from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class IsWorker(permissions.BasePermission):
    """
    Разрешение только для работников.
    """
    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        if not request.user.is_authenticated:
            return False

        # Получаем пользователя из базы данных
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return False

        # Проверяем, что пользователь в группе 'Workers'
        return user.groups.filter(name='Workers').exists()