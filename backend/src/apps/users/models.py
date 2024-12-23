from email.policy import default

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE

from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        TEACHER = 'T', 'Teacher'
        PARENT = 'P', 'Parent'
        CHILD = 'C', 'Child'

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=1, choices=Roles.choices, default='P')
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
    course = models.ForeignKey(Course, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Имя ребёнка: {self.name}, Имя родителя: {self.parent.user.username}"


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher')
