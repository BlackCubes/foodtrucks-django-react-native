from rest_framework import serializers

from .models import Truck, TruckImage

from main.utils import DynamicFieldsModelSerializer


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


class TruckSerializer(DynamicFieldsModelSerializer):
    """
    Serializer on the Truck model.

    Lookup Field: slug.

    Fields: uuid, name, slug, info, phone_number, email, website, products, images,
    and events.
    """
    images = TruckImageSerializer(many=True, read_only=True)

    want_profile_image = False

    class Meta:
        model = Truck
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'phone_number',
                  'email', 'website', 'images',)

    def __init__(self, *args, **kwargs):
        # An error would occur if this is not popped.
        extra_fields = kwargs.pop('extra_fields', None)

        # This is a safety check if `images` is in fields.
        fields = kwargs.get('fields', None)

        if extra_fields is not None and fields is not None:
            self.want_profile_image = 'profile_image' in extra_fields and 'images' in fields

        super(TruckSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if self.want_profile_image:
            profile_image = None

            if not representation['images']:
                profile_image = None
            else:
                for image_fields in representation['images']:
                    if image_fields['is_profile_image']:
                        profile_image = image_fields['image']
                        break

            representation.pop('images')

            representation['profile_image'] = profile_image

        return representation
