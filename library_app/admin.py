from django.contrib import admin

from library_app.models import (
    Fine,
    Borrow,
    LendPeriod,
    LibraryWorkingTime,
    Library
)


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_volume')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }

    def get_volume(self, obj):
        return f'{obj.volume} som'

    get_volume.short_description = 'Price'
    get_volume.admin_order_field = 'volume'


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'lend_from', 'book_return_date', 'lend_type')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }

    def lend_type(self, obj):
        return obj.book.lend_period.name

    lend_type.short_description = 'Lend type'
    lend_type.admin_order_field = 'book__lend_period__name'


@admin.register(LendPeriod)
class LendPeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'days_amount')

    css = {
        'all': ('resize-widget.css',),
    }


@admin.register(LibraryWorkingTime)
class LibraryWorkingTimeAdmin(admin.ModelAdmin):
    list_display = ('library', 'day_of_week', 'open_time', 'close_time')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }
