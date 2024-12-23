from rest_framework.views import APIView
from yaml import serialize

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


class AddChildView(APIView):

    def post(self, request):
        if request.user.role != 'P':  # Проверяем, что пользователь — родитель
            return Response({"error": "Only parents can add children"}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['parent_id'] = request.user.parent.id  # Привязываем ребенка к текущему родителю
        serializer = ChildCreationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Child added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def parent_children(request, id):
    children = Child.objects.filter(parent=id)
    serializer = ChildSerializer(children, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
