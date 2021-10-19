from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Review


# REVIEW INLINES
class ViewReviewInline(admin.TabularInline):
    """
    Inline Model Admin for viewing the Review model.
    """
    model = Review
    verbose_name = 'View Review'
    verbose_name_plural = 'View Reviews'

    extra = 0

    fields = ('review', 'product', 'user', 'created_at', 'updated_at',)
    readonly_fields = ('product', 'user', 'created_at', 'updated_at')

    def has_add_permission(self, request, obj=None):
        return False


class AddReviewInline(admin.TabularInline):
    """
    Inline Model Admin for adding to the Review model.
    """
    model = Review
    verbose_name = 'Add Review'
    verbose_name_plural = 'Add Reviews'

    extra = 0
    max_num = 1

    fields = ('review', 'product', 'user',)

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False


# REVIEW ADMIN
class ReviewAdmin(admin.ModelAdmin):
    """
    Model Admin for the Review model.
    """
    model = Review

    # View all reviews
    list_display = ('review', 'link_to_product',
                    'link_to_user', 'created_at', 'updated_at',)
    list_filter = ('product', 'user', 'product__truck',)
    search_fields = ('product__name', 'user__email', 'user__username',)
    ordering = ('-created_at',)

    # View and change one review
    fieldsets = (
        (None, {'fields': ('review', 'product', 'user',)}),
        ('Additional Info', {'fields': ('uuid', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ('uuid', 'created_at', 'updated_at', 'product', 'user',)

    # Add one review
    add_fieldset = (
        (None, {'fields': ('review', 'product', 'user',)}),
    )

    # Custom link to the product's change page.
    @admin.display(description='Product')
    def link_to_product(self, obj):
        link = reverse('admin:product_product_change', args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.product} ({obj.product.truck})')

    # Custom link to the user's change page.
    @admin.display(description='User')
    def link_to_user(self, obj):
        link = reverse('admin:user_customuser_change', args=[obj.user.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.user.username} ({obj.user})')

    def get_fieldsets(self, request, obj=None):
        if not obj:
            self.readonly_fields = []
            return self.add_fieldset
        self.readonly_fields = ('uuid', 'created_at',
                                'updated_at', 'product', 'user',)
        return super(ReviewAdmin, self).get_fieldsets(request, obj)


admin.site.register(Review, ReviewAdmin)
