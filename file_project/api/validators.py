from django.conf import settings
from rest_framework.exceptions import ValidationError


def validate_file_extension(value):
    file_extension = value.name.split('.')[-1]
    if file_extension not in settings.ALLOWED_EXTENSIONS_FILE:
        raise ValidationError('Недопустимое расширение файла.')
