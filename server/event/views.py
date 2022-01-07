from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Event
from .serializers import EventSerializer

from main.utils import final_success_response


class EventListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the Event model.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('date')

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)


class EventDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Event model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('date')
    lookup_field = 'uuid'

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)
