from django.contrib import admin

# Register your models here.

from django.db.models import QuerySet
from .models import Replenishment


@admin.register(Replenishment)
class ReplanishmantAdmin(admin.ModelAdmin):
    list_display = ['data','transactionid','description','amount','status']
