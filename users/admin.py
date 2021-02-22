from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.translation import gettext as _

from users.models import User, Librarian, Customer, Admin


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
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')
        }),
    )


@admin.register(Admin)
class BaseAdmin(UserAdmin):
    pass


@admin.register(Librarian)
class LibrarianAdmin(UserAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    pass
