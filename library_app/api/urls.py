from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from library_app.api.views import (
    LanguageApiViewSet,
    GenreApiViewSet,
    AuthorApiViewSet,
    PublisherApiViewSet,
    BookApiViewSet,
    LibraryApiViewSet,
    AddressApiViewSet
)

router = DefaultRouter()
router.register('languages', LanguageApiViewSet)
router.register('genres', GenreApiViewSet)
router.register('authors', AuthorApiViewSet)
router.register('publishers', PublisherApiViewSet)
router.register('books', BookApiViewSet)
router.register('address', AddressApiViewSet)
router.register('', LibraryApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
