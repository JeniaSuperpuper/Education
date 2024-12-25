import os
from celery import Celery

# Указываем Django-настройки для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Создаем экземпляр Celery
app = Celery('backend')

# Загружаем настройки из settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем задачи (tasks.py) в приложениях Django
app.autodiscover_tasks()