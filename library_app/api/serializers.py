from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers

from library_app.models import (
    Language,
    Genre,
    Author,
    Publisher,
    Book,
    BookProfile,
    Borrower
)
from users.models import User


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


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_year(self, year):
        if year and year > timezone.datetime.today().year:
            raise serializers.ValidationError("Book year must be less than current year")
        return year


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
        fields = ('id', 'reader', 'book', 'received_date', 'created', 'return_date', 'days_remain')

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
