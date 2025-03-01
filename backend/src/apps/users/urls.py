from django.urls import path
from apps.users import views

urlpatterns = [
    path('', views.UsersList.as_view(), name='user_list'),
    path('<int:pk>', views.UsersUpdateDelete.as_view(), name='user_up_del'),
    path('children', views.child_list, name='children'),
    path('register/parent', views.RegisterParentView.as_view(), name='register_parent'),
    path('add/child', views.AddChildView.as_view(), name='add_child'),
    path('parent/<int:id>/children', views.parent_children, name='parent_children'),

    path('register/', views.RegistrationView.as_view(), name='register'),
    path('verify-email/<str:uidb64>/<str:token>/', views.EmailVerificationView.as_view(), name='verify-email'),

    path('login', views.LoginView.as_view(), name='login'),
]
