from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    An Book class - to describe book in the system.
    """
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField(default=timezone.now().year)

    def __str__(self):
        return 'Book: ' + self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Author(models.Model):
    """
    Class defines book's author
    """
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()

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


class LendPeriods(models.Model):
    """
    Users can borrow books from library for different
    time period. This class defines frequently-used
    lending periods.
    """
    book = models.OneToOneField('Book', on_delete=models.CASCADE)
    days_amount = models.IntegerField()

    def __str__(self):
        return f'{self.book.title} for {self.days_amount} days.'

    class Meta:
        get_latest_by = "days_amount"
        ordering = ['days_amount']
        verbose_name = "Lending period"
        verbose_name_plural = "Lending periods"


class Borrower(models.Model):
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reader.name + " borrowed " + self.book.title

    @property
    def get_return_date(self):
        return self.issue_date.date() + timedelta(days=self.book.lendperiods.days_amount)
