from pathlib import Path

from PIL import Image
from celery import shared_task

from api.models import File


@shared_task
def process_pic(path: Path, pk):
    try:
        im = Image.open(path)
        im_resize_200_100 = im.resize((200, 100))
        im_path = Path(path)
        im_resize_200_100.save(im_path, 'JPEG')

        file = File.objects.get(pk=pk)
        file.processed = True
        file.save()

    except File.DoesNotExist:
        f'Запись файла не была найдена!'
