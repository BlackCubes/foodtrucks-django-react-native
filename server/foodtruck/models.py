import os
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4

from main.utils import slug_generator


def upload_truckimage_to(instance, filename):
    """
    Change the output of the image name.
    """
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000

    return f"images/truck/{instance.uuid}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


def upload_product_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000

    return f'images/product/{instance.uuid}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}'


class Truck(models.Model):
    """
    Truck model with fields of uuid, name, slug, info, phone_number, email, website,
    created_at, and updated_at.
    """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    info = models.TextField()
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class TruckImage(models.Model):
    """
    TruckImage model with fields of uuid, image, is_profile_image, created_at,
    updated_at, and truck.

    ForeignKey=Truck.
    """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    image = models.ImageField(upload_to=upload_truckimage_to)
    is_profile_image = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    truck = models.ForeignKey(
        Truck, related_name='images', on_delete=models.CASCADE)


pre_save.connect(slug_generator, sender=Truck)
