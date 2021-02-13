from rest_framework.viewsets import ModelViewSet

from library_app.api.permissions import IsAdminOrReadOnly, IsAdminOrLibrarianOrReadOnly
from library_app.api.serializers import LanguageSerializer, GenreSerializer, AuthorSerializer, PublisherSerializer, \
    BookSerializer, BookProfileSerializer, BorrowerSerializer
from library_app.models import Language, Genre, Author, Publisher, Book, BookProfile, Borrower


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
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class BookApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookProfileApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = BookProfileSerializer
    queryset = BookProfile.objects.all()


class BorrowerApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrLibrarianOrReadOnly,)
    serializer_class = BorrowerSerializer
    queryset = Borrower.objects.all()
