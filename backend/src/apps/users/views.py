from apps.users.serializers import UserSerializer
from apps.users.models import CustomUser
from rest_framework import generics


class UsersList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UsersUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


