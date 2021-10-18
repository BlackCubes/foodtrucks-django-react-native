from django.db import models
from uuid import uuid4


class Emoji(models.Model):
    """
    Emoji model with fields of uuid, emoji, name, created_at, and updated_at.
    """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    emoji = models.TextField()
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.emoji} ({self.name})'


class Like(models.Model):
    """
    Like model with fields of uuid, like, created_at, updated_at, emoji, and product.

    ForeignKeys: Emoji and Product.
    """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    like = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    emoji = models.ForeignKey(
        Emoji, related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(
        'product.Product', related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.like} {self.emoji} on {self.product} ({self.product.truck})'

    class Meta:
        verbose_name = 'Social'
