from rest_framework import serializers

from .models import Product
from review.serializers import ReviewSerializer
from social.serializers import LikeSerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer on the Product model.

    Lookup Field: slug.

    Fields: uuid, name, slug, info, image, price, quantity, is_available, truck,
    reviews, and likes.
    """
    truck = serializers.CharField(source='truck.slug')
    likes = LikeSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'image', 'price',
                  'quantity', 'is_available', 'truck', 'likes', 'reviews',)
