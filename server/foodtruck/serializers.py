from rest_framework import serializers

from .models import Truck, TruckImage

from main.utils import DynamicFieldsModelSerializer


class GetTruckProfileImageDynamicSerializer(DynamicFieldsModelSerializer):
    """
    A DynamicSerializer that gets the Foodtruck's profile image.

    If the `profile_image` is required, then when initializing the `TruckSerializer`,
    add in `fields` with `images` and `extra_fields` with `profile_image` as kwargs:
        `TruckSerializer(fields=('images',), extra_fields=('profile_image',))`.

    The `__init__` method is used to check if both `profile_image` and `images` are
    in the `extra_fields` and `fields` (respectively) to get the Truck's profile image
    in the `to_representation` method.

    The `to_representation` method is used to actually get the Truck's profile image, and
    set it in the JSON response while removing the `images` output.
    """
    want_profile_image = False

    def __init__(self, *args, **kwargs):
        # An error would occur if this is not popped.
        extra_fields = kwargs.pop('extra_fields', None)

        # This is a safety check if `images` is in fields.
        fields = kwargs.get('fields', None)

        if extra_fields is not None and fields is not None:
            self.want_profile_image = 'profile_image' in extra_fields and 'images' in fields

        super(GetTruckProfileImageDynamicSerializer,
              self).__init__(*args, **kwargs)

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


class TruckSerializer(GetTruckProfileImageDynamicSerializer):
    """
    Serializer on the Truck model. If the `profile_image` is required, then when
    initializing this serializer, add in `fields` with `images` and `extra_fields`
    with `profile_image` as kwargs:
        `TruckSerializer(fields=('images',), extra_fields=('profile_image',))`.

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
