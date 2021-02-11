from django.conf import settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib import admin


@admin.register(settings.User)
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'role']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser')}
         ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'role')
        }),
    )
