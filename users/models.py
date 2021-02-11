from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    TEACHER = 2
    STUDENT = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student')
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
