from rest_framework import serializers
from .models import CourseMessage

class CourseMessageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CourseMessage
        fields = ['id', 'course', 'user', 'text', 'created_at']