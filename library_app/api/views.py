from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from book_shelf.models import Book
from library_app.api.serializers import (
    LibrarySerializer, BorrowSerializer, CustomerBookSerializer
)
from library_app.models import (
    Library, Borrow
)
from users.models import Customer


class LibraryApiViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()


class BorrowApiView(ListCreateAPIView):
    serializer_class = BorrowSerializer
    queryset = Borrow.objects.all()


class CustomerBooksApiView(ListAPIView):
    serializer_class = CustomerBookSerializer
    queryset = Customer.objects.all()
