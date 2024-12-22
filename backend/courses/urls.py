from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<int:pk>', views.CourseUpdateDelete.as_view(), name='course_up_del'),
    path('category', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>', views.CategoryUpdateDelete.as_view(), name='category_up_del'),
    path('lesson', views.LessonList.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', views.LessonUpdateDelete.as_view(), name='lesson_up_del'),

    path('category/<slug:category_slug>/courses', views.CategoryCourseList.as_view(), name='category_course_list'),
    path('category/<slug:category_slug>/courses/<slug:slug>', views.CategoryCourseDetail.as_view(),
         name='category_course_detail'),
    path('category/<slug:category_slug>/courses/<slug:course_slug>/lessons', views.CategoryCourseLessonsList.as_view(),
         name='category_course_lessons_list'),
    path('category/<slug:category_slug>/courses/<slug:course_slug>/lessons/<slug:slug>',
         views.CategoryCourseLessonsDetail.as_view(),
         name='category_course_lessons_list'),

]
