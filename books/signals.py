from django.db.models.signals import (
    post_save,
    pre_save,
    post_delete,
    pre_delete,
    m2m_changed
)
from django.dispatch import receiver
from .models import Books

"======================PRE SAVE & POST SAVE==================="


# @receiver(pre_save, sender=Books)
# def pre_save_book(sender, instance, *args, **kwargs):
#     print("Kitob yaratilmoqda, Book id:", instance.id)
#
#
# @receiver(post_save, sender=Books)
# def post_save_book(sender, instance, created, *args, **kwargs):
#     if created:
#         print("Kitob yaratildi, Book id:", instance.id)
#     else:
#         print("Kitob yangilandi, Book id:", instance.id)


"======================PRE DELETE & POST DELETE==================="


# @receiver(pre_delete, sender=Books)
# def per_delete_book(sender, instance, *args, **kwargs):
#     print("Kiotb o'chirilmoqda book id:", instance.id)
#
#
# @receiver(post_delete, sender=Books)
# def post_delete_book(sender, instance,  *args, **kwargs):
#     print("Kitob o'chirildi book id:", instance.id)


"======================M2M CHANGED==================="


# @receiver(m2m_changed, sender=Books.author)
# def m2m_changed_book(sender, instance, action, *args, **kwargs):
#     print(action)
#     print(**kwargs)
#     print(" ")

