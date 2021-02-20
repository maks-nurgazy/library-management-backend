from django.contrib import admin

from library_app.models import (
    Author,
    Book,
    Genre,
    Language,
    Publisher
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author', 'publish_date')

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


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }
