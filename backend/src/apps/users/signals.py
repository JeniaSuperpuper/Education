from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Parent, Child, Teacher

@receiver(post_save, sender=CustomUser)
def create_related_profile(sender, instance, created, **kwargs):
    print(f"Сигнал сработал для пользователя {instance.email} с ролью {instance.role}")
    if created:
        if instance.role == "P":
            Parent.objects.create(user=instance)
        elif instance.role == "T":
            Teacher.objects.create(user=instance)


