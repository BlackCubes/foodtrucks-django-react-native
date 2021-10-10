from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the product model.

    Request Type: GET.
    """
    queryset = Product.objects.all().order_by('slug')
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Product model based on its slug.

    Lookup Field: slug.

    Request Type: GET.
    """
    queryset = Product.objects.all().order_by('slug')
    lookup_field = 'slug'
    serializer_class = ProductSerializer
