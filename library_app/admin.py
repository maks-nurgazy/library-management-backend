from django import forms
from django.contrib import admin

from library_app.models import (
    Author,
    Book,
    Genre,
    Language,
    BookProfile, Borrower

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
class GenreAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('get_author', 'get_books')

    def get_author(self, obj):
        return obj.full_name

    get_author.short_description = 'Author'
    get_author.admin_order_field = 'name'

    def get_books(self, obj):
        last_three = obj.book_set.all()[:3]
        return list(last_three)

    get_books.short_description = 'Books'

    css = {
        'all': ('resize-widget.css',),
    }


@admin.register(BookProfile)
class BookProfileAdmin(admin.ModelAdmin):
    list_display = ('book', 'book_amount', 'days_amount')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('get_reader', 'get_book', 'get_issue_date', 'return_date')

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(BorrowerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'reader':
            field.queryset = field.queryset.filter(role=3)
        return field

    def get_reader(self, obj):
        return obj.reader.full_name

    get_reader.short_description = 'Borrower'

    def get_book(self, obj):
        return obj.book.title

    get_book.short_description = 'Book name'

    def get_issue_date(self, obj):
        return obj.issue_date.date()

    get_issue_date.short_description = 'Issue date'

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }
