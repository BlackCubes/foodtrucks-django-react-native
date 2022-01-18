from django.db.models import fields
from rest_framework import serializers

from .models import Event
from foodtruck.models import Truck


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer on the Event model.

    Lookup Field: uuid.

    Fields: uuid, date, start_time, end_time, and truck.
    """
    truck = serializers.SlugRelatedField(
        slug_field='slug', queryset=Truck.objects.all(), many=True)

    class Meta:
        model = Event
        lookup_field = 'uuid'
        fields = ('uuid', 'date', 'start_time', 'end_time', 'truck',)
