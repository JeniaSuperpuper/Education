from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/course/<int:course_id>/', consumers.CourseChatConsumer.as_asgi()),
]