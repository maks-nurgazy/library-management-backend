from rest_framework.viewsets import ModelViewSet

from library_app.api.serializers import LanguageSerializer, GenreSerializer, AuthorSerializer, PublisherSerializer, \
    BookSerializer, BookProfileSerializer, BorrowerSerializer
from library_app.models import Language, Genre, Author, Publisher, Book, BookProfile, Borrower


class LanguageApiViewSet(ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class GenreApiViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class AuthorApiViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class PublisherApiViewSet(ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class BookApiViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookProfileApiViewSet(ModelViewSet):
    serializer_class = BookProfileSerializer
    queryset = BookProfile.objects.all()


class BorrowerApiViewSet(ModelViewSet):
    serializer_class = BorrowerSerializer
    queryset = Borrower.objects.all()
