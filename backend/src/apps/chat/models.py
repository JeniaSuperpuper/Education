from django.db import models
from apps.users.models import CustomUser, Course


class CourseMessage(models.Model):
    course = models.ForeignKey(Course, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='course_messages', on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.username}: {self.text}"