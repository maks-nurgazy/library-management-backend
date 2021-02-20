from django.contrib import admin
from django.forms import ModelForm
from django.utils import timezone

from library_app.models import (
    Author,
    Book,
    Genre,
    Language,
    BookProfile,
    Borrower,
    Publisher, ReaderDebt
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
    list_display = ('book', 'book_amount_total', 'get_remain_books', 'days_amount')

    # exclude = ['book_amount']

    def get_remain_books(self, obj):
        return obj.book_amount

    get_remain_books.short_description = 'Available'

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        uri = request.build_absolute_uri().split('/')[-2]
        if uri != 'change':
            field = super(BookProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
            if db_field.name == 'book':
                field.queryset = field.queryset.filter(book_profile=None)
            return field
        return super(BookProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('get_reader', 'get_book', 'received_date', 'return_date')

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(BorrowerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'reader':
            field.queryset = field.queryset.filter(role=3)
        if db_field.name == 'book':
            field.queryset = field.queryset.filter(book_profile__book_amount__gt=0)
        return field

    def get_reader(self, obj):
        return obj.reader.full_name

    get_reader.short_description = 'Borrower'

    def get_book(self, obj):
        return obj.book.title

    get_book.short_description = 'Book name'

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(ReaderDebt)
class ReaderDebtAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'debt')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }
