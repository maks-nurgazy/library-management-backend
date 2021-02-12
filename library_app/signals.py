from django.db.models.signals import post_save
from django.dispatch import receiver

from library_app.models import Borrower, BookProfile


@receiver(post_save, sender=Borrower)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        book_profile = instance.book.book_profile
        book_profile.book_amount = book_profile.book_amount - 1
        book_profile.save()
