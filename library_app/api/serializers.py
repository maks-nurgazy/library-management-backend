from rest_framework import serializers

from library_app.models import Language, Genre, Author, Publisher, Book, BookProfile, Borrower


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


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookProfile
        fields = '__all__'


class BorrowerSerializer(serializers.ModelSerializer):
    return_date = serializers.SerializerMethodField()

    class Meta:
        model = Borrower
        fields = ('id', 'reader', 'book', 'issue_date', 'created', 'return_date')

    def get_return_date(self, obj):
        return obj.return_date
