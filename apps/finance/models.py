import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from . import model_choices as mch
# Create your models here.


class Replenishment(models.Model):
    class StatusChoices(models.TextChoices):
        Plus = 'I', _('Зачислено')
        Minus = 'O', _('Выведено')
        Wait = 'W', _('Ожидание')

    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    data = models.DateTimeField(auto_now_add=True)
    transactionid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    description = models.PositiveSmallIntegerField(choices=mch.REQUEST_STATUSES)
    amount = models.PositiveIntegerField()
    status = models.CharField(
        max_length=2,
        choices=StatusChoices.choices,
        null=False,
    )

    def __str__(self):
        return f"{self.user}"

    # class Meta:
    #     uni

# class AmountInput(models.Model):
#     amount = models.ForeignKey(Replenishment, on_delete=models.CASCADE)
#     user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
#     # status = models.
#
# class AmountOutput(models.Model):
#     amount = models.ForeignKey(Replenishment, on_delete=models.CASCADE, )
#     user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
