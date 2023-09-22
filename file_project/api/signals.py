from django.db.models.signals import post_save
from django.dispatch import receiver

from api.tasks import process_pic
from api.models import File


@receiver(post_save, sender=File)
def process_file_on_save(sender, instance, **kwargs):
    if not instance.processed:
        process_pic.apply_async(
            args=[instance.file.path, instance.pk]
        )
