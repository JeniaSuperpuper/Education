from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_notification(subject, message, recipient_list):
    """
    Задача для отправки email.
    """
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,  # Используем переданный recipient_list
        fail_silently=False,  # Не игнорировать ошибки
    )
    return f"Email sent to {recipient_list}"