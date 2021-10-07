from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list or create a new one from the Review model.

    Request Type: GET and POST.
    """
    queryset = Review.objects.all().order_by('created_at')
    serializer_class = ReviewSerializer


class ReviewDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete on one from the Review model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET, PUT, PATCH, and DELETE.
    """
    queryset = Review.objects.all().order_by('created_at')
    lookup_field = 'uuid'
    serializer_class = ReviewSerializer
