from rest_framework.viewsets import ModelViewSet

from library_app.api.permissions import (
    IsAdminOrReadOnly,
)
from book_shelf.api.serializers import (
    LanguageSerializer,
    GenreSerializer,
    AuthorSerializer,
    PublisherSerializer,
    BookSerializer, BookDetailSerializer, AuthorDetailSerializer
)
from book_shelf.models import (
    Language,
    Genre,
    Author,
    Publisher,
    Book
)


class BookApiViewSet(ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            return BookDetailSerializer
        return BookSerializer


class LanguageApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class GenreApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class AuthorApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorSerializer


class PublisherApiViewSet(ModelViewSet):
    serializer_class = PublisherSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Publisher.objects.all()
