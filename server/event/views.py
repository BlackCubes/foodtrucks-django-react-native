from rest_framework import generics

from .models import Event
from .serializers import EventSerializer


class EventListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the Event model.

    Request Type: GET.
    """
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer


class EventDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Event model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET.
    """
    queryset = Event.objects.all().order_by('date')
    lookup_field = 'uuid'
    serializer_class = EventSerializer
