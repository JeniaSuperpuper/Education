from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Feedback
from .serializers import FeedbackSerializer
from .tasks import send_email_notification
from utils.ip_hacker_askar import IPRateLimiter
from django.utils import timezone

from utils.admin_emails import get_admin_emails
from .permissions import IsWorker
from rest_framework.permissions import AllowAny


class FeedbackView(APIView):
    """
    Создание нового обращения.
    """

    def post(self, request, *args, **kwargs):
        # Проверка лимита запросов
        limiter = IPRateLimiter(limit=5, period=60)  # 5 запросов в минуту
        allowed, message = limiter.check_limit(request)
        if not allowed:
            print('fsdfsdfsd')
            return Response({"error": message}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        # Обработка данных формы
        serializer = FeedbackSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Сохранение данных в базу
        ip = limiter.get_client_ip(request)
        feedback = Feedback(
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            message=serializer.validated_data['message'],
            ip_address=ip,
            category=serializer.validated_data.get('category', 'other'),
            attachment=serializer.validated_data.get('attachment'),
        )
        feedback.save()

        # Отправка уведомлений через Celery
        send_email_notification.delay(
            subject="Ваше сообщение получено",
            message="Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.",
            recipient_list=[serializer.validated_data['email']],
        )

        # Получение email администраторов
        admin_emails = get_admin_emails()
        if admin_emails:
            send_email_notification.delay(
                subject="Новое обращение",
                message=f"Получено новое обращение от {serializer.validated_data['name']} ({serializer.validated_data['email']}).\n\nСообщение: {serializer.validated_data['message']}",
                recipient_list=admin_emails,
            )

        return Response({"success": "Сообщение отправлено"}, status=status.HTTP_200_OK)

class FeedbackListView(APIView):
    """
    Получить список новых обращений (только для работников).
    """
    permission_classes = [IsWorker]  # Только для работников

    def get(self, request, *args, **kwargs):
        # Получаем только новые обращения
        feedbacks = Feedback.objects.filter(status='new')
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FeedbackTakeView(APIView):
    """
    Взять обращение в обработку (только для работников).
    """
    permission_classes = [IsWorker]  # Только для работников

    def patch(self, request, feedback_id, *args, **kwargs):
        try:
            feedback = Feedback.objects.get(id=feedback_id)
        except Feedback.DoesNotExist:
            return Response({"error": "Обращение не найдено"}, status=status.HTTP_404_NOT_FOUND)

        # Проверяем, что обращение еще не взято в обработку
        if feedback.status != 'new':
            return Response({"error": "Обращение уже в обработке или завершено"}, status=status.HTTP_400_BAD_REQUEST)

        # Меняем статус на "В обработке" и назначаем ответственного
        feedback.status = 'in_progress'
        feedback.assigned_to = request.user  # Текущий пользователь
        feedback.save()

        return Response({"success": f"Обращение взято в обработку работником {request.user.username}"}, status=status.HTTP_200_OK)

class FeedbackCompleteView(APIView):
    """
    Завершить обращение и отправить ответ пользователю (только для работников).
    """
    permission_classes = [IsWorker]  # Только для работников

    def patch(self, request, feedback_id, *args, **kwargs):
        try:
            feedback = Feedback.objects.get(id=feedback_id)
        except Feedback.DoesNotExist:
            return Response({"error": "Обращение не найдено"}, status=status.HTTP_404_NOT_FOUND)

        # Проверяем, что обращение в обработке
        if feedback.status != 'in_progress':
            return Response({"error": "Обращение не в обработке"}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем ответ от работника
        response_message = request.data.get('response_message')
        if not response_message:
            return Response({"error": "Необходимо указать ответ пользователю"}, status=status.HTTP_400_BAD_REQUEST)

        # Меняем статус на "Завершено"
        feedback.status = 'completed'
        feedback.completed_at = timezone.now()
        feedback.save()

        # Отправляем ответ пользователю
        send_email_notification.delay(
            subject="Ответ на ваше обращение",
            message=f"Ваше обращение от {feedback.created_at.strftime('%Y-%m-%d %H:%M')} было завершено.\n\nОтвет: {response_message}",
            recipient_list=[feedback.email],
        )

        return Response({"success": "Обращение завершено, ответ отправлен пользователю"}, status=status.HTTP_200_OK)