from rest_framework import serializers
from apps.users.models import CustomUser, Child, Parent
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            avatar=validated_data.get('avatar', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'





class ParentRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=32, required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'phone_number']

    def create(self, validated_data):
        password = validated_data.pop('password')
        phone_number = validated_data.pop('phone_number')
        user = CustomUser.objects.create(
            **validated_data,
            role='P'  # Устанавливаем роль родителя
        )
        user.set_password(password)
        user.save()
        Parent.objects.create(user=user, phone_number=phone_number)
        return user

class ChildCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128)
    age = serializers.IntegerField()
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all(), write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name', 'age', 'parent_id']

    def create(self, validated_data):
        parent = validated_data.pop('parent_id')
        password = validated_data.pop('password')
        name = validated_data.pop('name')
        age = validated_data.pop('age')

        user = CustomUser.objects.create(
            **validated_data,
            role='C',  # Устанавливаем роль ребенка
            username=validated_data['email'],  # Используем email как username
        )
        user.set_password(password)
        user.save()

        Child.objects.create(user=user, parent=parent, name=name, age=age)
        return user