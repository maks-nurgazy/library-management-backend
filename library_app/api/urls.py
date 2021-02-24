from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from library_app.api.views import (
    LibraryApiViewSet, BorrowApiView, CustomerBooksApiView
)

router = DefaultRouter()
router.register('libraries', LibraryApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrows/', BorrowApiView.as_view(), name='create_borrow'),
    path('customer/books', CustomerBooksApiView.as_view(), name='customer_books'),
]
