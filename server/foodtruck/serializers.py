from rest_framework import serializers

from server.event.models import Event

from .models import Product, Truck, TruckImage
from event.serializers import EventSerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer on the Product model.

    Lookup Field: slug.

    Fields: uuid, name, slug, info, image, price, quantity, is_available, truck,
    reviews, and likes.
    """
    truck = serializers.CharField(source='truck.slug')
    # TO DO: Add in reviews and likes fields

    class Meta:
        model = Product
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'image',
                  'price', 'quantity', 'is_available', 'truck',)


class TruckImageSerializer(serializers.ModelSerializer):
    """
    Serializer on the TruckImage model.

    Lookup Field: slug.

    Fields: uuid, image, is_profile_image, and truck.
    """
    truck = serializers.CharField(source='truck.slug')

    class Meta:
        model = TruckImage
        lookup_field = 'uuid'
        fields = ('uuid', 'image', 'is_profile_image', 'truck',)


class TruckSerializer(serializers.ModelSerializer):
    """
    Serializer on the Truck model.

    Lookup Field: slug.

    Fields: uuid, name, slug, info, phone_number, email, website, products, images,
    and events.
    """
    products = ProductSerializer(many=True, read_only=True)
    images = TruckImageSerializer(many=True, read_only=True)
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Truck
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'phone_number',
                  'email', 'website', 'products', 'images', 'events',)
