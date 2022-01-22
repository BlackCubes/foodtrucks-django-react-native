from rest_framework import serializers


from .models import Event

from foodtruck.serializers import TruckSerializer

from main.utils import get_request_view_name


class RemoveTruckRepresentationModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that removes the `truck` field from the output in order
    to avoid redundancy since we already know what type of foodtruck the list of
    events belongs to. This is known by the foodtruck's slug from the nested route:
    `/api/v1/foodtrucks/<slug>/events`.

    If one wants to know the detail of this foodtruck, they simply call another route:
    `/api/v1/foodtrucks/<slug>`.

    In other words, this route is only concern about getting all events from the foodtruck.

    The route this only targets: `/api/v1/foodtrucks/<slug>/events`.
    """

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        is_events_in_foodtruck_route = get_request_view_name(
            self.context['request'].path) == 'foodtrucks:event-list'

        if is_events_in_foodtruck_route:
            representation.pop('truck')

        return representation


class EventSerializer(RemoveTruckRepresentationModelSerializer):
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
