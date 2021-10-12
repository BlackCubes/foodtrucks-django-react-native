from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound

from .models import Product
from .serializers import ProductSerializer
from review.models import Review
from review.serializers import ReviewSerializer
from social.models import Like
from social.serializers import LikeSerializer


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


class ProductLikesModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Like and Product models. Tries to retrieve all
    likes based on the product's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Like: GET, POST, PATCH, PUT, DELETE.
    """
    queryset = Like.objects.all().select_related(
        'product').select_related('emoji').order_by('product__slug')
    serializer_class = LikeSerializer

    def get_queryset(self, *args, **kwargs):
        product_slug = self.kwargs.get('product_slug')

        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug does not exist.')

        return self.queryset.filter(product=product)


class ProductReviewsModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Review and Product models. Tries to retrieve all
    reviews based on the product's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Like: GET, POST, PATCH, PUT, DELETE.
    """
    queryset = Review.objects.all().select_related(
        'product').select_related('user').order_by('created_at')
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        product_slug = self.kwargs.get('product_slug')

        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug does not exist.')

        return self.queryset.filter(product=product)
