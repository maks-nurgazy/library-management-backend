from rest_framework import serializers

from book_shelf.api.serializers import BookSerializer
from book_shelf.models import Book
from library_app.exceptions import OnlyLibraryUseException
from library_app.models import (
    Library, Borrow
)
from users.models import Customer


class LibrarySerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Library
        fields = ('id', 'name', 'image', 'address')


class BorrowSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = serializers.CharField(source='customer.full_name', max_length=200, read_only=True)
    book = serializers.CharField(source='book.title', max_length=200, read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), write_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), write_only=True)
    lend_from = serializers.DateField()
    return_date = serializers.DateField(read_only=True)
    type = serializers.CharField(source='book.lend_period.name', read_only=True)

    def validate_book_id(self, book):
        if book.lend_period.days_amount == 0:
            raise OnlyLibraryUseException()
        return book

    def create(self, validated_data):
        customer = validated_data.pop('customer_id')
        book = validated_data.pop('book_id')
        print(customer.id)
        instance = Borrow.objects.create_book_borrower(customer=customer, book=book, **validated_data)
        return instance

    def update(self, instance, validated_data):
        pass


class CustomerBookSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'books')

    def get_books(self, customer):
        data = BorrowSerializer(customer.borrowed.all(), many=True).data
        for i in data:
            del i['customer']
        return data
