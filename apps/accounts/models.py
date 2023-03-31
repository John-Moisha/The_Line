import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager, UserManager
from .validators import *
from django.core.validators import FileExtensionValidator
from ..finance.models import Replenishment


def user_upload_avatar(instance, filename):
    path = f'{instance.id}/avatars/{filename}'
    return path


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        'email address', blank=False, null=False, unique=True,
    )

    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    avatar = models.FileField(null=True, blank=True, default=None,
                              upload_to=user_upload_avatar,
                              validators=[validate_file_avatar_size]
                              )
    # package_active = models.ForeignKey('packages.PackagesActive', on_delete=models.SET_NULL,
    #                                    null=True, default=None)
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(uuid.uuid4())

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
