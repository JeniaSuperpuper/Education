from rest_framework import generics
from apps.reviews.serializers import FeedbackSerializer, ReviewSerializer, LessonReviewSerializer
from apps.reviews.models import Feedback, Review, LessonReview


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class LessonReviewList(generics.ListCreateAPIView):
    queryset = LessonReview.objects.all()
    serializer_class = LessonReviewSerializer


class LessonReviewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonReview.objects.all()
    serializer_class = LessonReviewSerializer




