from django.contrib import admin

from .models import Emoji, Like


class EmojiAdmin(admin.ModelAdmin):
    """"""
    model = Emoji

    # View all emojis
    list_display = ('emoji', 'name', 'created_at', 'updated_at',)
    list_display_links = ('emoji', 'name',)
    list_filter = ('emoji', 'name',)
    search_fields = ('emoji', 'name',)
    ordering = ('name',)

    # View and changing one emoji
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


admin.site.register(Emoji, EmojiAdmin)
