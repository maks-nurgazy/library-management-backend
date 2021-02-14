from django.utils import timezone
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

    def to_representation(self, obj):
        ret = super(BookProfileSerializer, self).to_representation(obj)
        request = self.context.get('request', None)
        if request and request.user.role == 3:
            ret.pop('book_amount_total')
            ret.pop('book_amount')
        return ret


class BorrowerSerializer(serializers.ModelSerializer):
    return_date = serializers.SerializerMethodField()
    days_remain = serializers.SerializerMethodField()

    class Meta:
        model = Borrower
        fields = ('id', 'reader', 'book', 'issue_date', 'created', 'return_date', 'days_remain')

    def get_return_date(self, obj):
        return obj.return_date

    def get_days_remain(self, obj):
        delta = obj.return_date - timezone.datetime.today().date()
        return delta.days

    def to_representation(self, obj):
        ret = super(BorrowerSerializer, self).to_representation(obj)
        request = self.context.get('request', None)
        if request and request.user.role == 3:
            ret.pop('created')
        return ret
