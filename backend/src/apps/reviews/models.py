from django.db import models
from apps.courses.models import CustomUser, Course, Lesson
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    grade = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    content = models.CharField(
        max_length=256
    )

    def __str__(self):
        return f'Review from {self.user.username}'


class Review(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    grade = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    content = models.CharField(
        max_length=256
    )

    def __str__(self):
        return f'Review to {self.course.title} from {self.user.username}'


class LessonReview(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    grade = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    content = models.CharField(
        max_length=256
    )

    def __str__(self):
        return f'Review to {self.lesson.title} from {self.user.username}'