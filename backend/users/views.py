from django.shortcuts import render
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework import generics


class UsersList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

