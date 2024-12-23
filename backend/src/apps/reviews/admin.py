from django.contrib import admin
from apps.reviews.models import Review, Feedback, LessonReview


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'user', 'grade']


@admin.register(LessonReview)
class LessonReviewAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'user', 'grade']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'grade']