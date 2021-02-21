from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User, Librarian, Customer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

    def get_fields(self, *args, **kwargs):
        fields = super(UserSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            fields.pop('password')
        return fields

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

    def create(self, validated_data):
        role = validated_data.get('role', None)
        if role and role == 1:
            auth_user = User.objects.create_superuser(**validated_data)
        else:
            auth_user = User.objects.create_user(**validated_data)
        return auth_user


class LibrarianSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Librarian

    def create(self, validated_data):
        return Librarian.objects.create_librarian(**validated_data)


class CustomerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Customer

    def create(self, validated_data):
        return Customer.objects.create_customer(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email
            }
            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
