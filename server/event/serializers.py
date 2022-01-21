from rest_framework import serializers

from .models import Event

from foodtruck.serializers import TruckSerializer


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer on the Event model.

    Lookup Field: uuid.

    Fields: uuid, date, start_time, end_time, and truck.
    """
    truck = TruckSerializer(
        fields=('uuid', 'name', 'slug', 'images',), extra_fields=('profile_image',), many=True)

    class Meta:
        model = Event
        lookup_field = 'uuid'
        fields = ('uuid', 'date', 'start_time', 'end_time', 'truck',)
