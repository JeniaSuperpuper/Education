from rest_framework.views import APIView

from apps.users.serializers import UserSerializer, ChildSerializer, ParentRegistrationSerializer, \
    ChildCreationSerializer
from apps.users.models import CustomUser, Child, Parent
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpRequest
from rest_framework.response import Response


class UsersList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UsersUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def child_list(request: HttpRequest):
    """
    ПИСАЛ ЛЕГЕНДА КАРАПУЗОВИЧ

    :param request:
    :return:
    """
    child = Child.objects.all()
    serializer = ChildSerializer(child, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterParentView(APIView):
    def post(self, request):
        serializer = ParentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Parent registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parent, Child, CustomUser


class AddChildView(APIView):
    def post(self, request):
        parent_user = request.user
        if parent_user.role != "P":
            return Response({"error": "Только родитель может добавлять детей"}, status=status.HTTP_403_FORBIDDEN)

        child_name = request.data.get("name")
        child_age = request.data.get("age")

        if not child_name or not child_age:
            return Response({"error": "Имя и возраст обязательны"}, status=status.HTTP_400_BAD_REQUEST)

        parent = Parent.objects.get(user=parent_user)
        child_user = CustomUser.objects.create(username=child_name, role="C")
        child = Child.objects.create(name=child_name, age=child_age, user=child_user, parent=parent)

        return Response({"message": "Ребенок успешно добавлен", "child_id": child.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def parent_children(request, id):
    children = Child.objects.filter(parent=id)
    serializer = ChildSerializer(children, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
