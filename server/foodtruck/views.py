from rest_framework import generics

from .models import Product, Truck
from .serializers import ProductSerializer, TruckSerializer


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


# Product views:
class ProductListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the Product model.

    Request Type: GET.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Product model based on its slug.

    Lookup Field: slug.

    Request Type: GET.
    """
    queryset = Product.objects.all().order_by('name')
    lookup_field = 'slug'
    serializer_class = ProductSerializer
