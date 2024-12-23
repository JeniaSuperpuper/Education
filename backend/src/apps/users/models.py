from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    role = [
        ('T', 'Teacher'),
        ('S', 'Student')
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(choices=role, default='S', max_length=1)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email