from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny

from .models import Product
from .serializers import ProductSerializer

from main.utils import final_success_response

from review.models import Review
from review.serializers import ReviewSerializer

from social.models import Like
from social.serializers import LikeSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the product model.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('slug')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)


class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Product model based on its slug.

    Lookup Field: slug.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('slug')
    lookup_field = 'slug'

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)


class ProductLikesModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Like and Product models. Tries to retrieve all
    likes based on the product's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Like: GET, POST, PATCH, PUT, DELETE.
    """
    permission_classes = (AllowAny,)
    serializer_class = LikeSerializer
    queryset = Like.objects.all().select_related(
        'product').select_related('emoji').order_by('product__slug')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)

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
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().select_related(
        'product').select_related('user').order_by('created_at')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        product_slug = self.kwargs.get('product_slug')

        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug does not exist.')

        return self.queryset.filter(product=product)
