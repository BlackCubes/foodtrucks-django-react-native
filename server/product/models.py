import os
from django.db import models
from django.utils import timezone
from uuid import uuid4


def upload_to(instance, filename):
    """
    Change the output of the image name.
    """
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000

    return f'images/product/{instance.uuid}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}'


class Product(models.Model):
    """
    Product model with fields of uuid, name, slug, info, image, price, quantity,
    is_available, created_at, updated_at, and truck.

    ForeignKey=Truck.
    """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    name = models.CharField(max_length=182)
    slug = models.SlugField(max_length=182, null=True, blank=True)
    info = models.CharField(max_length=183)
    image = models.ImageField(upload_to=upload_to)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    truck = models.ForeignKey(
        'foodtruck.Truck', related_name='products', on_delete=models.CASCADE)
