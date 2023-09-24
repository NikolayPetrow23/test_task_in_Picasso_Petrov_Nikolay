from pathlib import Path

from PIL import Image, UnidentifiedImageError
from celery import shared_task

from api.utils import change_processed


@shared_task
def process_image(path: Path, pk):
    try:
        im = Image.open(path)
        im_resize_200_100 = im.resize((200, 100))
        im_path = Path(path)
        im_resize_200_100.save(im_path)

        change_processed(pk)

    except FileNotFoundError:
        return 'Запись файла не была найдена или не существует!'

    except UnidentifiedImageError:
        return 'Файл не идентифицирован!'

    except OSError:
        return 'Файл должен быть типа jpg, jpeg, png, или gif'


@shared_task
def process_text(path: Path, pk):
    try:
        with open(path, 'wb') as file:
            text = 'Файл был изменен!'
            text_bytes = text.encode('utf-8')
            file.write(text_bytes)

        change_processed(pk)

    except FileNotFoundError:
        return 'Запись файла не была найдена или не существует!'

    except TypeError:
        return 'Файл должен быть формата txt или text!'
