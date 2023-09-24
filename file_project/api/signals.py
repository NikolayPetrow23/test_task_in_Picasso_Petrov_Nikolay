from django.db.models.signals import post_save
from django.dispatch import receiver

from api.tasks import process_image, process_text
from api.models import File
from api.utils import check_type_file


@receiver(post_save, sender=File)
def process_file_on_save(sender, instance, **kwargs):
    if not instance.processed:
        type_file = check_type_file(instance)

        if type_file in ['jpg', 'jpeg', 'png', 'gif']:
            process_image.apply_async(
                args=[instance.file.path, instance.pk]
            )

        elif type_file in ['txt', 'text']:
            process_text.apply_async(
                args=[instance.file.path, instance.pk]
            )

        else:
            raise TypeError('Файл должен быть изображением или текстом!')
