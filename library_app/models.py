from datetime import timedelta, date

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User, Customer


# class Region(models.Model):  # Oblast
#     name = models.CharField(max_length=50)
#
#
# class District(models.Model):  # Rayon
#     name = models.CharField(max_length=50)
#     city = models.ForeignKey(Region, on_delete=models.CASCADE)
#
#
# class Address(models.Model):  # Concrete address
#     district = models.ForeignKey(District, on_delete=models.CASCADE)
#     location = models.CharField(max_length=50)


def library_image_directory(instance, filename):
    return f'library/{instance.name}/{filename}'


class Library(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=library_image_directory, null=True)
    address = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"

    def __str__(self):
        return self.name


class LibraryWorkingTime(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    day_of_week = models.SmallIntegerField(
        validators=[MaxValueValidator(7), MinValueValidator(1)]
    )
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        unique_together = ('library', 'day_of_week')
        verbose_name_plural = "Library working time"


class LendPeriod(models.Model):
    name = models.CharField(max_length=200)
    days_amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Borrow(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey('book_shelf.Book', on_delete=models.SET_NULL, null=True)
    lend_from = models.DateField(default=date.today)
    x_renewal = models.SmallIntegerField(editable=False, default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.full_name + " borrowed " + self.book.title

    @property
    def return_date(self):
        if hasattr(self.book, 'lend_period'):
            return self.lend_from + timedelta(days=self.book.lend_period.days_amount)
        return self.lend_from + timedelta(days=3)

    class Meta:
        ordering = ['created']


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reader_debt')
    bill = models.FloatField(default=0.0)


class Fine(models.Model):
    name = models.CharField(max_length=50)
    volume = models.PositiveIntegerField()
