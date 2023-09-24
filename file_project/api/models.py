from django.db import models

from api.validators import validate_file_extension


class File(models.Model):
    file = models.FileField(upload_to='file', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-uploaded_at',)
