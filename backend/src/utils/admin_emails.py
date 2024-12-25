from django.contrib.auth import get_user_model
from django.core.cache import cache

User = get_user_model()

def get_admin_emails():
    """
    Получение email всех администраторов с кэшированием
    """
    cache_key = "admin_emails"
    admin_emails = cache.get(cache_key)
    print(admin_emails)

    if not admin_emails:
        admins = User.objects.filter(is_staff=True)
        admin_emails = [admin.email for admin in admins if admin.email]
        cache.set(cache_key, admin_emails, timeout=60 * 60)  # Кэшируем на 1 час
    print(admin_emails)
    return admin_emails