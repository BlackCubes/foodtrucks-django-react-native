from django.contrib import admin
from django.utils.html import format_html

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Model Admin for the Product model.
    """
    model = Product

    # Viewing all products
    list_display = ('name', 'truck', 'quantity', 'is_available',
                    'created_at', 'updated_at', 'image_tag',)
    list_display_links = ('name', 'truck',)
    list_filter = ('name', 'truck', 'is_available',)
    search_fields = ('name', 'truck__name',)
    ordering = ('slug',)

    # Viewing and changing on product
    fieldsets = (
        (None, {'fields': ('name', 'info', 'price',
         'quantity', 'is_available', 'truck',)}),
        ('Product Image', {'fields': ('image', 'image_tag')}),
        ('Additional Info', {
         'fields': ('uuid', 'slug', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ('uuid', 'slug', 'created_at',
                       'updated_at', 'image_tag',)

    # Adding one new product
    add_fieldset = (
        (None, {'fields': ('name', 'info', 'price',
         'quantity', 'is_available', 'truck',)}),
    )

    # Adding preview image.
    @admin.display(description='Preview')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{0}" style="width: 45px; height: 45px;" />'.format(obj.image.url))
        else:
            return '(No image)'

    # To display the add_fielsets on the creation page.
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldset
        return super(ProductAdmin, self).get_fieldsets(request, obj)


admin.site.register(Product, ProductAdmin)
