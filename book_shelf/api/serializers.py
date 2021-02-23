from django.utils import timezone
from rest_framework import serializers

from book_shelf.models import (
    Language,
    Genre,
    Author,
    Publisher,
    Book,
)


class BookSerializer(serializers.ModelSerializer):
    book_author = serializers.CharField(source='author.full_name', read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'summary', 'isbn', 'book_author', 'publish_date', 'page_size', 'book_format', 'author',
                  'publisher', 'lend_period', 'genre', 'language')
        extra_kwargs = {
            'publisher': {'write_only': True},
            'page_size': {'write_only': True},
            'lend_period': {'write_only': True},
            'language': {'write_only': True},
            'genre': {'write_only': True},
            'author': {'write_only': True}
        }

    def get_read_author(self, obj):
        return obj.author.full_name

    def validate_year(self, year):
        if year and year > timezone.datetime.today().year:
            raise serializers.ValidationError("Book year must be less than current year")
        return year


class BookDetailSerializer(BookSerializer):
    book_publisher = serializers.CharField(source='publisher.name', read_only=True)
    book_lend_type = serializers.CharField(source='lend_period.name', read_only=True)
    book_genre = serializers.SerializerMethodField(read_only=True)
    book_language = serializers.SerializerMethodField(read_only=True)

    class Meta(BookSerializer.Meta):
        fields = ('id', 'title', 'summary', 'isbn', 'book_author', 'publish_date', 'page_size', 'book_format', 'author',
                  'publisher', 'book_publisher', 'genre', 'book_genre', 'language', 'book_language', 'lend_period',
                  'book_lend_type')
        extra_kwargs = {
            'author': {'write_only': True},
            'publisher': {'write_only': True},
            'lend_period': {'write_only': True},
            'genre': {'write_only': True},
            'language': {'write_only': True},
        }

    def get_book_genre(self, obj):
        genres = [val.get('name') for val in obj.genre.values('name')]
        return genres

    def get_book_language(self, obj):
        languages = [val.get('name') for val in obj.language.values('name')]
        return languages


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate_date_of_birth(self, date_of_birth):
        if date_of_birth > timezone.datetime.today().date():
            raise serializers.ValidationError("You can't predict authors birthdate")
        return date_of_birth

    def validate_date_of_death(self, date_of_death):
        if date_of_death and date_of_death > timezone.datetime.today().date():
            raise serializers.ValidationError("You can't predict authors death")
        return date_of_death

    def validate(self, data):
        date_of_death = data['date_of_death']
        if date_of_death and data['date_of_birth'] > date_of_death:
            raise serializers.ValidationError({"date_of_death": "must occur after birth"})
        return data


class AuthorDetailSerializer(AuthorSerializer):
    books = serializers.SerializerMethodField()

    def get_books(self, obj):
        print(obj.book_set.all())
        return BookSerializer(obj.book_set, many=True).data

    class Meta(AuthorSerializer.Meta):
        fields = ('name', 'surname', 'date_of_birth', 'date_of_death', 'books')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
