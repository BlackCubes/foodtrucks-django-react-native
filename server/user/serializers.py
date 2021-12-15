from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer on the User model.

    Fields: email and password.

    Logins the user.
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, validators=[
                                     validate_password], write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email is required.')

        if password is None:
            raise serializers.ValidationError('A password is required.')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Sorry, could not find your account.')

        if not user.is_active:
            raise serializers.ValidationError('User has been deactivated.')

        return {
            'email': user.email,
            'username': user.username,
        }


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer on the User model.

    Fields: email, username, password, and password_confirmation.

    Creates a new user.
    """
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=CustomUser.objects.all(), message='This email already exists.')])
    username = serializers.CharField(required=True, min_length=4, max_length=25, validators=[
                                     UniqueValidator(queryset=CustomUser.objects.all(), message='This username already exists.')])
    password = serializers.CharField(required=True, validators=[
                                     validate_password], write_only=True)
    password_confirmation = serializers.CharField(
        required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'password_confirmation')

    def validate_password_confirmation(self, password_confirmation):
        data = self.get_initial()

        password = data.get('password')

        if password != password_confirmation:
            raise serializers.ValidationError('The passwords do not match.')

        return password_confirmation

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'], username=validated_data['username'])

        user.set_password(validated_data['password'])
        user.save()

        return user
