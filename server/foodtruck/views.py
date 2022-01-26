from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny

from .models import Truck
from .serializers import TruckSerializer

from event.models import Event
from event.serializers import EventSerializer

from main.utils import final_success_response

from product.models import Product
from product.serializers import ProductSerializer

from review.models import Review
from review.serializers import ReviewSerializer

from social.models import Like
from social.serializers import LikeSerializer


# Truck views:
class TruckListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the Truck model.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = TruckSerializer
    queryset = Truck.objects.all().order_by('name')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)


class TruckDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Truck model based on its slug.

    Lookup Field: slug.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = TruckSerializer
    queryset = Truck.objects.all().order_by('name')
    lookup_field = 'slug'

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)


class TruckEventsModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Event and Truck models. Tries to retrieve all
    events based on the truck's slug.

    Actions Only: list.

    Request Type Only: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer
    queryset = Event.objects.all().prefetch_related('truck').order_by('date')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        truck_slug = self.kwargs.get('truck_slug')

        try:
            truck = Truck.objects.get(slug=truck_slug)
        except Truck.DoesNotExist:
            raise NotFound('A foodtruck with this slug does not exist.')

        return self.queryset.filter(truck=truck)


class TruckProductsModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Product and Truck models. Tries to retrieve all
    likes based on the truck's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Synonymous: GET, POST, PATCH, PUT, DELETE.
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all().select_related('truck').order_by('slug')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        truck_slug = self.kwargs.get('truck_slug')

        try:
            truck = Truck.objects.get(slug=truck_slug)
        except Truck.DoesNotExist:
            raise NotFound('A foodtruck with this slug does not exist.')

        return self.queryset.filter(truck=truck)


class TruckLikesModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Like and Truck models. Tries to retrieve all
    likes based on the truck's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Synonymous: GET, POST, PATCH, PUT, DELETE.
    """
    permission_classes = (AllowAny,)
    serializer_class = LikeSerializer
    queryset = Like.objects.all().select_related(
        'product').select_related('emoji').order_by('product__slug')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        truck_slug = self.kwargs.get('truck_slug')

        try:
            truck = Truck.objects.get(slug=truck_slug)
        except Truck.DoesNotExist:
            raise NotFound('A foodtruck with this slug does not exist.')

        return self.queryset.filter(product__truck=truck)


class TruckReviewsModelViewSet(viewsets.ModelViewSet):
    """
    Model viewset on the Review and Truck models. Tries to retrieve all
    reviews based on the truck's slug, if a GET request.

    Actions: list, create, retrieve, update, partial_update, destroy.

    Request Synonymous: GET, POST, PATCH, PUT, DELETE.
    """
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().select_related(
        'product').select_related('user').order_by('created_at')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        truck_slug = self.kwargs.get('truck_slug')

        try:
            truck = Truck.objects.get(slug=truck_slug)
        except Truck.DoesNotExist:
            raise NotFound('A foodtruck with this slug does not exist.')

        return self.queryset.filter(product__truck=truck)
