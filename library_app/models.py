from django.contrib.auth.models import User
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
    year = models.DateField(default=timezone.now())

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
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    days_amount = models.IntegerField()

    def __str__(self):
        return f'{self.book.title} {self.days_amount}'

    class Meta:
        get_latest_by = "days_amount"
        ordering = ['days_amount']
        verbose_name = "Lending period"
        verbose_name_plural = "Lending periods"


class Publisher(models.Model):
    """
    Class defines book's publisher
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return 'Publisher: %s' % self.name

    class Meta:
        get_latest_by = "name"
        ordering = ['name']
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
