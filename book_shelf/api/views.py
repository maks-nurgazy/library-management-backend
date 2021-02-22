from rest_framework.viewsets import ModelViewSet

from library_app.api.permissions import (
    IsAdminOrReadOnly,
)
from book_shelf.api.serializers import (
    LanguageSerializer,
    GenreSerializer,
    AuthorSerializer,
    PublisherSerializer,
    BookSerializer
)
from book_shelf.models import (
    Language,
    Genre,
    Author,
    Publisher,
    Book
)


class BookApiViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


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
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class PublisherApiViewSet(ModelViewSet):
    serializer_class = PublisherSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Publisher.objects.all()
