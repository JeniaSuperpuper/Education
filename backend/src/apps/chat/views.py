from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CourseMessage
from .serializers import CourseMessageSerializer

class CourseMessageViewSet(viewsets.ModelViewSet):
    queryset = CourseMessage.objects.all()
    serializer_class = CourseMessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)