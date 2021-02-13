from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from library_app.models import Borrower, BookProfile


@receiver(post_save, sender=Borrower)
def add_borrower(sender, instance, created, **kwargs):
    if created:
        book_profile = instance.book.book_profile
        book_profile.book_amount = book_profile.book_amount - 1
        book_profile.save()


@receiver(post_delete, sender=Borrower)
def remove_borrower(sender, instance, **kwargs):
    book_profile = instance.book.book_profile
    book_profile.book_amount = book_profile.book_amount + 1
    book_profile.save()
