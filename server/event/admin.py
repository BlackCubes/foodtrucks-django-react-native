from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Model Admin for the Event model.
    """
    model = Event

    # Viewing all events.
    list_display = ('date', 'get_foodtrucks', 'start_time', 'end_time',)
    list_filter = ('date',)
    search_fields = ('date',)
    ordering = ('-date',)

    # Viewing and changing one event.
    fieldsets = (
        (None, {'fields': ('date', 'start_time', 'end_time', 'truck',)}),
        ('Additional Info', {'fields': ('uuid',)}),
    )
    readonly_fields = ('uuid',)

    # Adding one new event.
    add_fieldsets = (
        (None, {'fields': ('date', 'start_time', 'end_time', 'truck',)}),
    )

    # To save extra queries since this is a many-to-many.
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('truck')

    # To display the foodtrucks in list_display (DON'T EVER DO THIS!).
    @admin.display(description='Foodtrucks')
    def get_foodtrucks(self, obj):
        return ', '.join([t.name for t in obj.truck.all()])

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(EventAdmin, self).get_fieldsets(request, obj)


admin.site.register(Event, EventAdmin)
