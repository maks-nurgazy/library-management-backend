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
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            response = {
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }
            return Response(response, status=status_code)
        else:
            return Response("not valid", status=status.HTTP_400_BAD_REQUEST)
