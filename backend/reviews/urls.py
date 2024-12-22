from django.urls import path
from . import views


urlpatterns = [
    path('feedbacks', views.FeedbackList.as_view(), name='feedback_list'),
    path('feedbacks/<int:pk>', views.FeedbackUpdateDelete.as_view(), name='feedback_up_del'),
    path('', views.ReviewList.as_view(), name='reviews_list'),
    path('<int:pk>', views.ReviewUpdateDelete.as_view(), name='reviews_up_del'),
]