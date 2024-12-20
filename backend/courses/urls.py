from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<int:pk>', views.CourseUpdateDelete.as_view(), name='course_up_del'),
    path('category', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>', views.CategoryUpdateDelete.as_view(), name='category_up_del'),
]