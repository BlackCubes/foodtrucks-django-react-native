from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer on the User model.

    Fields: email, username, password, and password_confirmation.

    Creates a new user.
    """
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=CustomUser.objects.all())])
    username = serializers.CharField(
        required=True, min_length=4, max_length=25)
    password = serializers.CharField(required=True, validators=[
                                     validate_password], write_only=True)
    password_confirmation = serializers.CharField(
        required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'password_confirmation')

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({
                'password': 'The password and its confirmation do not match.',
            })

        return data

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'], username=validated_data['username'])

        user.set_password(validated_data['password'])
        user.save()

        return user
