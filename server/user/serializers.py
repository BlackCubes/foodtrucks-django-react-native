from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer on the User model.

    Fields: old_password, old_password_confirmation, and new_password.

    Changes the user's password.
    """
    old_password = serializers.CharField(required=True, validators=[validate_password], error_messages={
        'required': 'The old password is required.',
        'blank': 'The old password cannot be empty.'
    }, write_only=True)
    old_password_confirmation = serializers.CharField(required=True, error_messages={
        'required': 'The old password confirmation is required.',
        'blank': 'The old password confirmation cannot be empty.'
    }, write_only=True)
    new_password = serializers.CharField(required=True, validators=[validate_password], error_messages={
        'required': 'The new password is required.',
        'blank': 'The new password cannot be empty.'
    }, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'old_password_confirmation',
                  'new_password', 'token',)
        read_only_fields = ('token',)

    def validate_old_password(self, old_password):
        user = self.context['request'].user

        if not user.check_password(old_password):
            raise serializers.ValidationError(
                'The old password is not correct.')

        return old_password

    def validate_old_password_confirmation(self, old_password_confirmation):
        data = self.get_initial()

        old_password = data.get('password', None)

        if old_password is None:
            raise serializers.ValidationError('Your old password is required.')

        if old_password != old_password_confirmation:
            raise serializers.ValidationError('The passwords do not match.')

        return old_password_confirmation

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer on the User model.

    Fields: email and password.

    Logins the user.
    """
    email = serializers.EmailField(required=True, error_messages={
        'required': 'The email is required.',
        'blank': 'The email cannot be empty.'
    })
    password = serializers.CharField(required=True, validators=[validate_password], error_messages={
        'required': 'The password is required.',
        'blank': 'The password cannot be empty.'
    }, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'token',)

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
            'token': user.token,
        }


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer on the User model.

    Fields: email, username, password, and password_confirmation.

    Creates a new user.
    """
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=CustomUser.objects.all(), message='This email already exists.')], error_messages={
            'required': 'The email is required.',
            'blank': 'The email cannot be empty.'
    })
    username = serializers.CharField(required=True, min_length=4, max_length=25, validators=[
        UniqueValidator(queryset=CustomUser.objects.all(), message='This username already exists.')], error_messages={
            'required': 'The username is required.',
            'blank': 'The username cannot be empty.'
    })
    password = serializers.CharField(required=True, validators=[
        validate_password], error_messages={
            'required': 'The password is required.',
            'blank': 'The password cannot be empty.'
    }, write_only=True)
    password_confirmation = serializers.CharField(required=True, error_messages={
        'required': 'The password confirmation is required.',
        'blank': 'The password confirmation cannot be empty.'
    }, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password',
                  'password_confirmation', 'token',)

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


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer on the User model.

    Fields: email and username.

    Changes the user's email and/or username.
    """
    email = serializers.EmailField(required=False, validators=[
        UniqueValidator(queryset=CustomUser.objects.all(), message='This email already exists.')], error_messages={
            'blank': 'The email cannot be empty.'
    })
    username = serializers.CharField(required=False, min_length=4, max_length=25, validators=[
        UniqueValidator(queryset=CustomUser.objects.all(), message='This username already exists.')], error_messages={
            'blank': 'The username cannot be empty.'
    })

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'token',)
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        if password is not None:
            raise serializers.ValidationError(
                "This route is not for changing passwords. Please use '/change-password' to change your password.")

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
