from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Emoji, Like


# EMOJI ADMIN
class EmojiAdmin(admin.ModelAdmin):
    """
    Model Admin for the Emoji model. 
    """
    model = Emoji

    # View all emojis
    list_display = ('emoji', 'name', 'created_at', 'updated_at',)
    list_display_links = ('emoji', 'name',)
    list_filter = ('emoji', 'name',)
    search_fields = ('emoji', 'name',)
    ordering = ('name',)

    # Viewing and changing one emoji
    fieldsets = (
        (None, {'fields': ('emoji', 'name',)}),
        ('Additional Info', {'fields': ('uuid', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ('uuid', 'created_at', 'updated_at',)

    # Adding one new emoji
    add_fieldset = (
        (None, {'fields': ('emoji', 'name')}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldset
        return super(EmojiAdmin, self).get_fieldsets(request, obj)


# LIKE INLINES
class ViewLikeInline(admin.TabularInline):
    """
    Inline Model Admin for viewing the Like model.
    """
    model = Like
    verbose_name = 'View Social'
    verbose_name_plural = 'View Socials'

    extra = 0

    fields = ('like', 'emoji', 'created_at', 'updated_at',)
    readonly_fields = ('like', 'emoji', 'created_at', 'updated_at',)

    def has_add_permission(self, request, obj=None):
        return False


class AddLikeInline(admin.TabularInline):
    """
    Inline Model Admin for the adding to the Like model.
    """
    model = Like
    verbose_name = 'Add Social'
    verbose_name_plural = 'Add Socials'

    extra = 0
    max_num = 1

    fields = ('like', 'emoji',)

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False


# LIKE ADMIN
class LikeAdmin(admin.ModelAdmin):
    """
    Model Admin for the Like model.
    """
    model = Like

    # View all likes
    list_display = ('like', 'link_to_emoji', 'link_to_product',
                    'created_at', 'updated_at',)
    list_display_links = ('like',)
    list_filter = ('like', 'emoji', 'product',)
    search_fields = ('like', 'emoji__emoji', 'emoji__name', 'product__name',)
    ordering = ('-like',)

    # Viewing and changing one like
    fieldsets = (
        ('Additional Info', {'fields': ('uuid', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ('uuid', 'created_at', 'updated_at',)

    # Adding one new like
    add_fieldset = (
        (None, {'fields': ('like', 'emoji', 'product',)}),
    )

    # Custom link to the emoji's change page instead of the like change page.
    @admin.display(description='Emoji')
    def link_to_emoji(self, obj):
        link = reverse('admin:social_emoji_change', args=[obj.emoji.id])
        return format_html('<a href="{}">{}</a>', link, obj.emoji)

    # Custom link to the product's change page.
    @admin.display(description='Product')
    def link_to_product(self, obj):
        link = reverse('admin:product_product_change', args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', link, obj.product)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldset
        return super(LikeAdmin, self).get_fieldsets(request, obj)


admin.site.register(Emoji, EmojiAdmin)
admin.site.register(Like, LikeAdmin)
