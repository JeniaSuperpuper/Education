from django.db import models



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
    teachers = models.ForeignKey('users.Teacher', on_delete=models.CASCADE, related_name='courses_as_teacher')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title = models.CharField(
        max_length=128
    )
    slug = models.SlugField(
        max_length=128
    )
    number = models.PositiveSmallIntegerField()
    description = models.TextField(
        max_length=512
    )
    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Lesson "{self.title}" in {self.course.title}'
