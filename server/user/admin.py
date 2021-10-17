from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
        ('Profile Image', {'fields': ('profile_image',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Additional Info', {
         'fields': ('uuid', 'date_joined', 'last_login',)}),
    )
    readonly_fields = ('uuid', 'date_joined', 'last_login',)

    # Adding one new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1',
                       'password2', 'is_staff', 'is_active',)
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
