from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    roles = [
        ('T', 'Teacher'),
        ('P', 'Parent'),
        ('C', 'Child'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(choices=roles, default='P', max_length=1)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=32)

    def __str__(self):
        return self.user.username


class Child(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveSmallIntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='child')

    def __str__(self):
        return f"Имя ребёнка: {self.name}, Имя родителя: {self.parent.user.username}"


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True, blank=True)
