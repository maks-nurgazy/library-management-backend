from datetime import timedelta, date

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User, Customer


class Region(models.Model):  # Oblast
    name = models.CharField(max_length=50)


class City(models.Model):  # Gorod
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Region, on_delete=models.CASCADE)


class District(models.Model):  # Rayon
    name = models.CharField(max_length=50)
    city = models.ForeignKey(Region, on_delete=models.CASCADE)


class Address(models.Model):  # Concrete address
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)


def library_image_directory(instance, filename):
    return f'library/{instance.name}/{filename}'


class Library(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=library_image_directory, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)


class LibraryWorkingTime(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    day_of_week = models.SmallIntegerField(
        validators=[MaxValueValidator(7), MinValueValidator(1)]
    )
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        unique_together = ('library', 'day_of_week')


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=200,
                            help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Language(models.Model):
    name = models.CharField(unique=True, max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    """
    Class defines book's author
    """
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return 'Author: ' + self.name + ' ' + self.surname

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    class Meta:
        get_latest_by = "name"
        ordering = ['name', 'surname']
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Publisher(models.Model):
    """
    Class defines book's publisher
    """
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return 'Publisher: %s' % self.name

    class Meta:
        get_latest_by = "name"
        ordering = ['name']
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"


class LendPeriod(models.Model):
    name = models.CharField(max_length=200)
    days_amount = models.PositiveSmallIntegerField()


class BookFormat(models.Model):
    name = models.CharField(max_length=50, help_text="E-book, pdf, audio etc...")


class Book(models.Model):
    """
    An Book class - to describe book in the system.
    """
    title = models.CharField(max_length=200)
    summary = models.TextField(null=True, blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    publish_date = models.PositiveSmallIntegerField(default=timezone.now().year)
    page_size = models.PositiveSmallIntegerField()
    lend_period = models.ForeignKey('LendPeriod', models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Borrow(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    lend_from = models.DateField(default=date.today)
    x_renewal = models.SmallIntegerField(editable=False, default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.full_name + " borrowed " + self.book.title

    @property
    def return_date(self):
        if hasattr(self.book, 'book_profile'):
            return self.lend_from + timedelta(days=self.book.book_profile.days_amount)
        return self.lend_from + timedelta(days=3)

    class Meta:
        ordering = ['created']


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reader_debt')
    bill = models.FloatField(default=0.0)


class Fine(models.Model):
    name = models.CharField(max_length=50)
    volume = models.PositiveIntegerField()
