import os
from django.core.exceptions import ValidationError


MAX_UPLOAD_SIZE = 0.8 * 1024 * 1024


def validate_file_extension(value):
    # ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    # valid_extensions = ['.jpeg', '.jpg', '.png']
    # if not ext.lower() in valid_extensions:
    #     raise ValidationError('Unsupported file extension.')
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Error message')


def validate_file_avatar_size(value):
    file_size = value.size

    if file_size > MAX_UPLOAD_SIZE:
        raise ValidationError(f"Допустимый размер файла {MAX_UPLOAD_SIZE / 1024} kb")
    else:
        return value
