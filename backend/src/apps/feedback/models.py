from django.db import models
from django.conf import settings

class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ("support", "Техническая поддержка"),
        ("payment", "Вопрос по оплате"),
        ("other", "Другое"),
    ]

    STATUS_CHOICES = [
        ("new", "Новое"),
        ("in_progress", "В обработке"),
        ("completed", "Завершено"),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя", db_index=True)
    email = models.EmailField(verbose_name="Email", db_index=True)
    message = models.TextField(verbose_name="Сообщение")
    ip_address = models.GenericIPAddressField(verbose_name="IP адрес")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other", verbose_name="Категория")
    attachment = models.FileField(upload_to='feedback_attachments/', null=True, blank=True, verbose_name="Прикрепленный файл")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="new", verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата завершения")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ответственный",
        related_name="feedback_assigned"  # Уникальное имя для обратной связи
    )

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f"{self.name} - {self.email} ({self.status})"