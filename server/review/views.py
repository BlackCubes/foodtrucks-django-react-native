from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Review
from .serializers import ReviewSerializer

from main.utils import final_success_response


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list or create a new one from the Review model.

    Request Type: GET and POST.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('created_at')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)


class ReviewDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete on one from the Review model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET, PUT, PATCH, and DELETE.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('created_at')
    lookup_field = 'uuid'

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)
