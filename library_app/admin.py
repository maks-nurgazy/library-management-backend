from django.contrib import admin

from library_app.models import (
    Author,
    Book,
    Genre,
    Language,
    LendPeriods

)


@admin.register(Book, Genre, Language)
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
