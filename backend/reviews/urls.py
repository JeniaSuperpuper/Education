from django.urls import path
from . import views


urlpatterns = [
    path('feedbacks', views.FeedbackList.as_view(), name='feedback_list'),
    path('feedbacks/<int:pk>', views.FeedbackUpdateDelete.as_view(), name='feedback_up_del'),
    path('courses', views.ReviewList.as_view(), name='reviews_list'),
    path('courses/<int:pk>', views.ReviewUpdateDelete.as_view(), name='reviews_up_del'),
    path('lessons', views.LessonReviewList.as_view(), name='lesson_reviews_list'),
    path('lessons/<int:pk>', views.LessonReviewUpdateDelete.as_view(), name='lesson_reviews_up_del'),
]