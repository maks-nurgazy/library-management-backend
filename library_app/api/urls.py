from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from library_app.api.views import (
    LibraryApiViewSet, BorrowApiView, CustomerBooksApiView, CurrentUserBorrowView, BorrowRenewalApiView, FineApiViewSet
)

router = DefaultRouter()
router.register('libraries', LibraryApiViewSet)
router.register('fines', FineApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrows/', BorrowApiView.as_view(), name='create_borrow'),
    path('borrowbook/', CurrentUserBorrowView.as_view(), name='current_user_borrow'),
    path('user/borrows/', CurrentUserBorrowView.as_view(), name='logged_user_borrow'),
    path('borrow/renewal/', BorrowRenewalApiView.as_view(), name='borrow_renewal'),
    path('customer/books/', CustomerBooksApiView.as_view(), name='customer_books'),
]
