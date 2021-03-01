from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from book_shelf.models import Book
from library_app.api.permissions import IsAdminOrReadOnly, IsAdminOrLibrarianOrReadOnly, IsAdminOrLibrarianOrSubmitOnly
from library_app.api.serializers import (
    LibrarySerializer, BorrowSerializer, CustomerBookSerializer, CurrentUserBorrowSerializer, FineSerializer
)
from library_app.models import (
    Library, Borrow, Fine, DebtUser
)
from users.models import Customer


class LibraryApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()


class FineApiViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = FineSerializer
    queryset = Fine.objects.all()


class BorrowApiView(ListCreateAPIView):
    permission_classes = (IsAdminOrLibrarianOrReadOnly,)
    serializer_class = BorrowSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Borrow.objects.all()
        return_date = self.request.query_params.get('return-date', None)
        if return_date is not None:
            if return_date == 'finish':
                queryset = queryset.filter(returned=False)
                queryset = (x for x in queryset if x.return_date < timezone.now().date())
                queryset = sorted(queryset, key=lambda t: t.return_date)
            elif return_date == 'after':
                queryset = queryset.filter(returned=False)
                queryset = (x for x in queryset if x.return_date > timezone.now().date())
                queryset = sorted(queryset, key=lambda t: t.return_date)

        return queryset


class CustomerBooksApiView(ListAPIView):
    permission_classes = (IsAdminOrLibrarianOrReadOnly,)
    serializer_class = CustomerBookSerializer
    queryset = Customer.objects.all()


class CurrentUserBorrowView(ListCreateAPIView):
    permission_classes = (IsAdminOrLibrarianOrSubmitOnly,)
    serializer_class = CurrentUserBorrowSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Borrow.objects.filter(Q(customer=user) & Q(returned=False))
        return queryset

    def delete(self, request, *args, **kwargs):
        borrow_id = self.request.data['borrow_id']
        borrow = Borrow.objects.get(id=borrow_id)
        if borrow.returned:
            response = f'You did not taken book with id = {borrow_id}'
            return Response({'error': response})
        if borrow.return_date < timezone.now().date():
            date = timezone.now().date() - borrow.return_date
            debt = borrow.book.lend_period.fine.volume * date.days
            DebtUser.objects.create(customer=self.request.user, debt=debt)
            return Response({'debt': debt, 'returned': borrow_id})
        borrow.returned = True
        borrow.save()
        return Response({'returned': borrow_id})


class BorrowRenewalApiView(APIView):
    permission_classes = (IsAdminOrLibrarianOrReadOnly,)

    def post(self, request, *args, **kwargs):
        borrow_id = self.request.data['borrow_id']
        borrow = Borrow.objects.get(id=borrow_id)
        if borrow.x_renewal < 3 and borrow.return_date > timezone.now().date():
            borrow.x_renewal += 1
            borrow.save()
            return Response(BorrowSerializer(instance=borrow).data)
        return Response({'error': 'You cannot renew this book'})
