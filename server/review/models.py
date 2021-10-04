from django.db import models
from uuid import uuid4


class Review(models.Model):
    """
    Review model with fields of uuid, review, created_at, updated_at, product,
    and user.

    ForeignKeys: Product and User.
    """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    review = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    product = models.ForeignKey(
        'foodtruck.Product', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        'user.CustomUser', related_name='reviews', on_delete=models.CASCADE)
