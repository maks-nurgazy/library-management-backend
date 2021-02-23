from django.test import TestCase

from library_app.models import Library
from users.models import Admin


class LibraryCreateTests(TestCase):
    def setUp(self):
        data = {
            'first_name': 'Admin',
            'last_name': 'Admin',
            'email': 'admin@test.com',
            'password': 'admin'
        }
        self.admin = Admin.objects.create(**data)

    @classmethod
    def setUpTestData(cls):
        pass

    def test_library_create(self):
        data = {
            'name': 'Library of Kyrgyzstan',
            'address': 'Bishkek, Djal 27'
        }
        library = Library.objects.create(**data)
        self.assertTrue(library.id)
