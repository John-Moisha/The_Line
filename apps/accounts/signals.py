from django.db.models.signals import post_save, pre_delete
# from django.contrib.auth.models import User
from apps.accounts.models import CustomUser
from django.dispatch import receiver
# from apps.dashboard.models import (Check, Verification, Transaction)


# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Check.objects.create(user=instance)
#         Verification.objects.create(user=instance)
#         Transaction.objects.create(user=instance)
#     instance.money.save()
#     instance.trans.save()
#     instance.verif.save()






        # Verification.objects.create(user=instance)
        # Transaction.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.check.save()
#     instance.verification.save()
#     instance.transaction.save()
