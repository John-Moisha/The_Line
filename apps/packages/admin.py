from django.contrib import admin

# Register your models here.

from .models import Package, PackagesActive


@admin.register(Package)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ['name','period','percent']


@admin.register(PackagesActive)
class PackagesActiveAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'start_amount','start_date_package',
                    'end_amount','end_date_package']
