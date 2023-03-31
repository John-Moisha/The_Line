from django.db import models

# Create your models here.


class Package(models.Model):
    # user = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL,
    #                          null=True, default=None)
    name = models.TextField()
    period = models.PositiveSmallIntegerField()
    percent = models.PositiveSmallIntegerField()
    min_amount = models.PositiveSmallIntegerField()
    max_amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}"


class PackagesActive(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL,
                             null=True, default=None)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL,
                                null=True, default=None)
    # amount = models.FloatField()
    start_amount = models.FloatField()
    start_date_package = models.DateTimeField(auto_now_add=True)
    end_amount = models.FloatField()
    end_date_package = models.DateTimeField()

    def __str__(self):
        return f"{self.package} "




# class Replenishment(models.Model):
#     class StatusChoices(models.TextChoices):
#         Plus = 'I', _('Зачислено')
#         Minus = 'O', _('Выведено')
#         Wait = 'W', _('Ожидание')
#
#     user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
#
#     data = models.DateTimeField(auto_now_add=True)
#     transactionid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     description = models.PositiveSmallIntegerField(choices=mch.REQUEST_STATUSES)
#     amount = models.PositiveIntegerField()
#     status = models.CharField(
#         max_length=2,
#         choices=StatusChoices.choices,
#         null=False,
#     )
#
#     def __str__(self):
#         return f"{self.user}"