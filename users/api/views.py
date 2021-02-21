from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.api.permissions import AdminOnly
from users.api.serializers import (
    UserSerializer,
    UserLoginSerializer,
    LibrarianSerializer, CustomerSerializer,
)
from users.models import User, Librarian, Customer


class UserApiViewSet(ModelViewSet):
    permission_classes = (AdminOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LibrarianViewSet(ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UserLoginView(GenericAPIView):
    """ User login url """
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid()
        if valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
