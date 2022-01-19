from rest_framework import serializers

from .models import Product

from foodtruck.serializers import TruckSerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer on the Product model.

    Lookup Field: slug.

    Fields: uuid, name, slug, info, image, price, quantity, is_available, truck,
    reviews, and likes.
    """
    truck = TruckSerializer(fields=('uuid', 'name', 'slug',))

    class Meta:
        model = Product
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'image', 'price',
                  'quantity', 'is_available', 'truck',)
