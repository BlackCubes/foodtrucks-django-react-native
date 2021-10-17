import os
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from uuid import uuid4

from .managers import CustomUserManager


def upload_to(instance, filename):
    """
    Change the output of the photo name.
    """
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 100

    return f"images/user/{instance.uuid}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=25, validators=[
                                MinLengthValidator(4)])
    profile_image = models.ImageField(upload_to=upload_to)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
