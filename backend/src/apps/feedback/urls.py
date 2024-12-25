from django.urls import path
from .views import FeedbackView, FeedbackListView, FeedbackTakeView, FeedbackCompleteView

urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback'),
    path('new/', FeedbackListView.as_view(), name='feedback-list'),
    path('<int:feedback_id>/take/', FeedbackTakeView.as_view(), name='feedback-take'),
    path('<int:feedback_id>/complete/', FeedbackCompleteView.as_view(), name='feedback-complete'),
]