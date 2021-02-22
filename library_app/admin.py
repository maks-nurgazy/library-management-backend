from django.contrib import admin


from library_app.models import (
    Account,
    Fine,
    Borrow,
    LendPeriod,
    LibraryWorkingTime,
    Library
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('customer', 'bill')

    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('resize-widget.css',),
        }


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'lend_from', 'return_date', 'lend_type')

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
