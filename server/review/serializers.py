from rest_framework import serializers

from .models import Review
from product.models import Product
from user.models import CustomUser


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer on the Review model.

    Lookup Field: uuid.

    Fields: uuid, review, created_at, updated_at, product, and user.
    """
    product = serializers.SlugRelatedField(
        slug_field='slug', queryset=Product.objects.all())
    user = serializers.SlugRelatedField(
        slug_field='uuid', queryset=CustomUser.objects.all())

    class Meta:
        model = Review
        lookup_field = 'uuid'
        fields = ('uuid', 'review', 'created_at',
                  'updated_at', 'product', 'user',)
