from django.core.cache import cache
from django.http import HttpRequest
from datetime import timedelta

class IPRateLimiter:
    def __init__(self, limit=5, period=60):
        self.limit = limit  # Максимальное количество запросов
        self.period = period  # Период времени в секундах

    def get_client_ip(self, request: HttpRequest) -> str:
        """
        Получает IP-адрес клиента.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            print(ip, 'fddsfsd')
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(ip, 'sdxz')
        return ip

    def check_limit(self, request: HttpRequest) -> tuple[bool, str]:
        """
        Проверяет, не превышен ли лимит запросов для IP.
        """
        ip = self.get_client_ip(request)
        cache_key = f'rate_limit:{ip}'
        request_count = cache.get(cache_key, 0)

        if request_count >= self.limit:
            return False, "Превышен лимит запросов. Попробуйте позже."

        cache.set(cache_key, request_count + 1, self.period)
        return True, "Лимит не превышен"