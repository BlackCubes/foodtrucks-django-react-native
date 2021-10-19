from django.contrib import admin
from django.utils.html import format_html

from .models import Truck, TruckImage
from event.admin import AddEventInline, ViewEventInline
from product.admin import ProductInline


# TRUCK IMAGE INLINE
class TruckImageInline(admin.StackedInline):
    """
    Inline Model Admin for the TruckImage model.
    """
    model = TruckImage

    fieldsets = (
        (None, {
            'fields': ('image', 'image_tag',
                       'is_profile_image', 'created_at', 'updated_at',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'image_tag')
    min_num = 1
    max_num = 3

    # Adding preview image.
    @admin.display(description='Preview')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{0}" style="width: 45px; height: 45px;" />'.format(obj.image.url))
        else:
            return '(No image)'


# TRUCK ADMIN
class TruckAdmin(admin.ModelAdmin):
    """
    Model Admin for the Truck model.

    Inlines: TruckImageInline.
    """
    model = Truck

    # Viewing all trucks
    list_display = ('name', 'email', 'phone_number',
                    'created_at', 'updated_at', 'image_tag',)
    list_filter = ('name', 'email',)
    search_fields = ('name', 'email',)
    ordering = ('name',)

    # Viewing and changing one truck
    fieldsets = (
        (None, {'fields': ('name', 'info',)}),
        ('Contact', {'fields': ('email', 'phone_number', 'website',)}),
        ('Additional Info', {
         'fields': ('uuid', 'slug', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ('uuid', 'slug', 'created_at',
                       'updated_at', 'image_tag',)

    # Adding one new truck
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'info',)
        }),
        ('Contact', {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'website',),
        }),
    )

    # To be viewed on the truck since the these models have a foreign key.
    inlines = (TruckImageInline, ProductInline,
               AddEventInline, ViewEventInline,)

    # Adding preview image from the TruckImage.
    @admin.display(description='Preview')
    def image_tag(self, obj):
        queryset = TruckImage.objects.filter(
            truck=obj).filter(is_profile_image=True)

        if len(queryset):
            if queryset[0].image:
                return format_html('<img src="{0}" style="width: 45px; height: 45px;" />'.format(queryset[0].image.url))

        return '(No profile image)'

    # To display the add_fieldsets on the creation page.
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(TruckAdmin, self).get_fieldsets(request, obj)

    # To not display the inlines on the creation page.
    def get_inline_instances(self, request, obj):
        return obj and super(TruckAdmin, self).get_inline_instances(request, obj) or []


admin.site.register(Truck, TruckAdmin)
