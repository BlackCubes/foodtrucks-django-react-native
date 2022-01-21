from rest_framework import serializers

from .models import Product

from foodtruck.serializers import TruckSerializer

from main.utils import get_request_view_name


class RemoveProductRepresentationModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that removes the `truck` field from the output in order
    to avoid redundancy since we already know what type of foodtruck the list of
    products belongs to. This is known by the foodtruck's slug from the nested route:
    `/api/v1/foodtrucks/<slug>/products`.

    If one wants to know the detail of this foodtruck, they simply call another route:
    `/api/v1/foodtrucks/<slug>`.

    In other words, this route is only concern about getting all products from the foodtruck.

    The route this only targets: `/api/v1/foodtrucks/<slug>/products`.
    """

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        is_products_in_foodtruck_route = get_request_view_name(
            self.context['request'].path) == 'foodtrucks:product-list'

        if is_products_in_foodtruck_route:
            representation.pop('truck')

        return representation


class ProductSerializer(RemoveProductRepresentationModelSerializer):
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
