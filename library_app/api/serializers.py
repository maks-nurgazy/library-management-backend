from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers

from library_app.models import (
    Library, Borrow
)


class LibrarySerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Library
        fields = ('id', 'name', 'image', 'address')


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'
