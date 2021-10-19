from django.db import models
from uuid import uuid4


class Event(models.Model):
    """
    Event model with fields of uuid, date, start_time, end_time, and truck.

    ManyToMany: Truck.
    """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    truck = models.ManyToManyField('foodtruck.Truck', related_name='events')

    def __str__(self):
        return f'Event Date: {self.date}'
