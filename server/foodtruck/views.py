from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound

from .models import Truck
from .serializers import TruckSerializer
from product.models import Product
from product.serializers import ProductSerializer
from social.models import Like
from social.serializers import LikeSerializer


# Truck views:
class TruckListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the Truck model.

    Request Type: GET.
    """
    queryset = Truck.objects.all().order_by('name')
    serializer_class = TruckSerializer


class TruckDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Truck model based on its slug.

    Lookup Field: slug.

    Request Type: GET.
    """
    queryset = Truck.objects.all().order_by('name')
    lookup_field = 'slug'
    serializer_class = TruckSerializer


class TruckProductsModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Product and Truck models. Tries to retrieve all
    likes based on the truck's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Synonymous: GET, POST, PATCH, PUT, DELETE.
    """
    queryset = Product.objects.all().select_related('truck').order_by('slug')
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        truck_slug = self.kwargs.get('truck_slug')

        try:
            truck = Truck.objects.get(slug=truck_slug)
        except Truck.DoesNotExist:
            raise NotFound('A truck with this slug does not exist.')

        return self.queryset.filter(truck=truck)


class TruckLikesModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Like and Truck models. Tries to retrieve all
    likes based on the truck's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Synonymous: GET, POST, PATCH, PUT, DELETE.
    """
    queryset = Like.objects.all().select_related(
        'product').select_related('emoji').order_by('product__slug')
    serializer_class = LikeSerializer

    def get_queryset(self, *args, **kwargs):
        truck_slug = self.kwargs.get('truck_slug')

        try:
            truck = Truck.objects.get(slug=truck_slug)
        except Truck.DoesNotExist:
            raise NotFound('A truck with this slug does not exist.')

        return self.queryset.filter(product__truck=truck)
