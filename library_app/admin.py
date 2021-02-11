from django import forms
from django.contrib import admin

from library_app.models import (
    Author,
    Book,
    Genre,
    Language,
    LendPeriods, Borrower

)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author', 'year')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }

    def get_author(self, obj):
        return obj.author.full_name

    get_author.short_description = 'Author'
    get_author.admin_order_field = 'title'


@admin.register(Genre)
class BookAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Language)
class BookAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    css = {
        'all': ('resize-widget.css',),
    }


@admin.register(LendPeriods)
class BookLendPeriodAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(BorrowerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'reader':
            field.queryset = field.queryset.filter(role=3)
        return field

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }
