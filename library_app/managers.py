from django.db.models import Manager


class BorrowManager(Manager):
    def create_book_borrower(self, customer, book, **extra_fields):
        borrow = self.model(customer=customer, book=book, **extra_fields)
        borrow.save()
        return borrow
