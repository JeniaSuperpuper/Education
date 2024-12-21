from rest_framework import serializers
from .models import CustomUser
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
            username = validated_data['username'],
            email = validated_data['email'],
            role = validated_data['role'],
            avatar = validated_data.get('avatar', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user