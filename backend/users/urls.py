from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersList.as_view(), name='user_list'),
]