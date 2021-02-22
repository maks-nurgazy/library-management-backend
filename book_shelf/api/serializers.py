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
    class Meta:
        model = Book
        fields = '__all__'

    def validate_year(self, year):
        if year and year > timezone.datetime.today().year:
            raise serializers.ValidationError("Book year must be less than current year")
        return year


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
