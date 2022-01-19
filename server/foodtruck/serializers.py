from rest_framework import serializers

from .models import Truck, TruckImage


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
    images = TruckImageSerializer(many=True, read_only=True)

    class Meta:
        model = Truck
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'phone_number',
                  'email', 'website', 'images',)
