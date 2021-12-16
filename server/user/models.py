import jwt
import os
from datetime import datetime, timedelta
from django.conf import settings
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

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(minutes=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
