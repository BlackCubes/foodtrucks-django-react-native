from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import CustomUser


# USER ADMIN
class CustomUserAdmin(UserAdmin):
    """
    Admin Form for CustomUser by subclassing UserAdmin.
    """
    model = CustomUser

    # Viewing all users
    list_display = ('username', 'email', 'is_staff', 'is_superuser',
                    'is_active', 'date_joined', 'last_login',)
    list_filter = ('username', 'email', 'is_staff',
                   'is_superuser', 'is_active',)
    search_fields = ('username', 'email',)
    ordering = ('username',)

    # Viewing and changing one user
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        ('Profile Image', {'fields': ('profile_image', 'image_tag',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Additional Info', {
         'fields': ('uuid', 'date_joined', 'last_login',)}),
    )
    readonly_fields = ('uuid', 'date_joined', 'last_login', 'image_tag',)

    # Adding one new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1',
                       'password2', 'is_staff', 'is_active',)
        }),
    )

    # Adding preview image.
    def image_tag(self, obj):
        if obj.profile_image:
            return format_html('<img src="{0}" style="width: 45px; height: 45px;" />'.format(obj.profile_image.url))
        else:
            return '(No image)'
    image_tag.short_description = 'Preview'


admin.site.register(CustomUser, CustomUserAdmin)
