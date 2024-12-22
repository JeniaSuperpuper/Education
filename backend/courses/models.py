from django.db import models
from users.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    teachers = models.ManyToManyField(CustomUser, related_name='courses_as_teacher')
    students = models.ManyToManyField(CustomUser, related_name='courses_as_student', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
