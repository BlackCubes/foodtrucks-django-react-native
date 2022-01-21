from rest_framework import serializers

from .models import Product

from foodtruck.serializers import TruckSerializer

from main.utils import get_request_view_name


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer on the Product model.

    Lookup Field: slug.

    Fields: uuid, name, slug, info, image, price, quantity, is_available, truck,
    reviews, and likes.
    """
    truck = TruckSerializer(
        fields=('uuid', 'name', 'slug', 'images',), extra_fields=('profile_image',))

    class Meta:
        model = Product
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'image', 'price',
                  'quantity', 'is_available', 'truck',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # This is to check if it is on the route `/api/v1/foodtrucks/<slug>/products/`.
        is_products_in_foodtruck_route = get_request_view_name(
            self.context['request'].path) == 'foodtrucks:product-list'

        if is_products_in_foodtruck_route:
            # If it is in the route `/api/v1/foodtrucks/<slug>/products/`, then remove
            # the `truck` key since this route shows all products from the foodtruck
            # (removes redundancy).
            representation.pop('truck')

        return representation
