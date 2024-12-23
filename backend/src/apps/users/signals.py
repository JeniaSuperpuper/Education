from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Parent, Child, Teacher


@receiver(post_save, sender=CustomUser)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "P":
            Parent.objects.create(user=instance)

        elif instance.role == 'C':
            parent = Parent.objects.first()
            Child.objects.create(user=instance, parent=parent)

        elif instance.role == "T":
            Teacher.objects.create(user=instance)
