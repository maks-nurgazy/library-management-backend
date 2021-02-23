from django.test import TestCase

from users.models import Admin, Librarian, Customer


class UserTests(TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        pass

    def test_admin_created(self):
        data = {
            "first_name": "admin",
            "last_name": "admin",
            "email": "admin@test.com",
            "password": "admin"
        }
        admin = Admin.objects.create_user(**data)
        self.assertTrue(admin.id)
        self.assertEqual(admin.role, "ADMIN")
        self.assertTrue(admin.check_password('admin'))
        self.assertFalse(admin.check_password('asldfla'))

    def test_customer_created(self):
        data = {
            "first_name": "customer",
            "last_name": "custom",
            "email": "customer@test.com",
            "password": "customer"
        }
        customer = Customer.objects.create_user(**data)
        self.assertTrue(customer.id)
        self.assertEqual(customer.role, "CUSTOMER")
        self.assertTrue(customer.check_password('customer'))
        self.assertFalse(customer.check_password('Customer'))

    def test_librarian_created(self):
        data = {
            "first_name": "librarian",
            "last_name": "librarian",
            "email": "librarian@test.com",
            "password": "librarian"
        }
        librarian = Librarian.objects.create_user(**data)
        self.assertTrue(librarian.id)
        self.assertEqual(librarian.role, "LIBRARIAN")
        self.assertTrue(librarian.check_password('librarian'))
        self.assertFalse(librarian.check_password('libraryan'))
