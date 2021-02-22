from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book_shelf.api.views import BookApiViewSet
from book_shelf.api.views import LanguageApiViewSet
from book_shelf.api.views import GenreApiViewSet
from book_shelf.api.views import AuthorApiViewSet
from book_shelf.api.views import PublisherApiViewSet

book_shelf = DefaultRouter()
book_shelf.register('books', BookApiViewSet)
book_shelf.register('languages', LanguageApiViewSet)
book_shelf.register('genres', GenreApiViewSet)
book_shelf.register('authors', AuthorApiViewSet)
book_shelf.register('publishers', PublisherApiViewSet)

urlpatterns = [
    path('', include(book_shelf.urls)),
]
