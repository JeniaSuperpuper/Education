from django.urls import path
from apps.users import views


urlpatterns = [
    path('', views.UsersList.as_view(), name='user_list'),
    path('<int:pk>', views.UsersUpdateDelete.as_view(), name='user_up_del'),
]