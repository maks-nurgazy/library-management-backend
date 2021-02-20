from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users.managers import AdminManager, LibrarianManager, CustomerManager, AdminManager


class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        LIBRARIAN = "LIBRARIAN", "Librarian"
        CUSTOMER = "CUSTOMER", "Customer"

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(choices=Roles.choices, blank=True, null=True, default="CUSTOMER", max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    objects = AdminManager()

    def __str__(self):
        return self.email


class Admin(User):
    base_type = User.Roles.ADMIN
    objects = AdminManager()

    class Meta:
        proxy = True


class Librarian(User):
    base_type = User.Roles.LIBRARIAN
    objects = LibrarianManager()

    class Meta:
        proxy = True


class Customer(User):
    base_type = User.Roles.CUSTOMER
    objects = CustomerManager()

    class Meta:
        proxy = True
