from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers

from library_app.models import (
    Library
)
from users.models import User


# class RegionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Region
#         fields = '__all__'
#
#
# class DistrictSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = District
#         fields = '__all__'
#
#
# class AddressSerializer(serializers.Serializer):
#     province = serializers.CharField(max_length=30, help_text='Область')
#     city = serializers.CharField(max_length=30, help_text='Город')
#     district = serializers.CharField(max_length=30, help_text='Район')
#     location = serializers.CharField(max_length=30, help_text='улица Минкуш, 80')
#
#     class Meta:
#         fields = ('province', 'city', 'district', 'location')
#
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         pass


class LibrarySerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Library
        fields = ('id', 'name', 'image', 'address')
