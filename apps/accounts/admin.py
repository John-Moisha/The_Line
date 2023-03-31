from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email',
                    # 'package_active',
                    'unique_id']

# from django.contrib.auth import get_user_model
#
# user = get_user_model()
#
# admin.site.register(user)


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [
#                     # 'first_name',
#                     # 'last_name',
#                     'email',
#                     'unique_id',
#                     ]
#
#
# admin.site.register(CustomUser, ProfileAdmin)
# admin.site.register(User, ProfileAdmin)


# @admin.register(CustomUser)
# class UserAdmin(admin.ModelAdmin):
#     pass


