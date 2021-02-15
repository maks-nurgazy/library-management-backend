from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet

from library_app.api.permissions import (
    IsAdminOrReadOnly,
    IsAdminOrLibrarianOrReadOnly
)
from library_app.api.serializers import (
    LanguageSerializer,
    GenreSerializer,
    AuthorSerializer,
    PublisherSerializer,
    BookSerializer,
    BookProfileSerializer,
    BorrowerSerializer
)
from library_app.models import (
    Language,
    Genre,
    Author,
    Publisher,
    Book,
    BookProfile,
    Borrower
)


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


class BookApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookProfileApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = BookProfileSerializer
    queryset = BookProfile.objects.all()


class BorrowerApiViewSet(LoginRequiredMixin, ModelViewSet):
    permission_classes = (IsAdminOrLibrarianOrReadOnly,)
    serializer_class = BorrowerSerializer
    queryset = Borrower.objects.all()

    def get_queryset(self):
        if self.request.user.role == 3:
            try:
                queryset = Borrower.objects.filter(reader=self.request.user)
            except ObjectDoesNotExist:
                queryset = []
        else:
            queryset = Borrower.objects.all()
        return queryset
