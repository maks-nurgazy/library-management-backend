from django.db import models
from django.utils import timezone


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


class BookFormat(models.Model):
    name = models.CharField(max_length=50, help_text="E-book, pdf, audio etc...")

    def __str__(self):
        return self.name


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
    language = models.ManyToManyField('Language')
    publish_date = models.PositiveSmallIntegerField(default=timezone.now().year)
    page_size = models.PositiveSmallIntegerField()
    book_format = models.CharField(max_length=50, choices=[(i.name, i.name) for i in BookFormat.objects.all()],
                                   default="Paper")
    lend_period = models.ForeignKey('library_app.LendPeriod', models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"
