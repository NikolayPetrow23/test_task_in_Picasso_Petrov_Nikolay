import shutil
import tempfile
import time

from api.models import File
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings, TestCase
from rest_framework.test import APITestCase

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
NUMBER_OF_OBJECT_FILE = 3
LAST_ITEM_FILE = 4


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class FileProjectAPITest(APITestCase):
    fixtures = ['files.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.name_images = 'test_images.jpeg'
        cls.image_path = f'test_data/{cls.name_images}'

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        time.sleep(1)
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class FileUnitTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.name_images = 'test_images.jpeg'
        cls.image_path = f'test_data/{cls.name_images}'

        with open(cls.image_path, 'rb') as image_file:
            image_data = image_file.read()
            cls.image = SimpleUploadedFile(
                cls.name_images,
                image_data,
                content_type='image/jpeg'
            )

        cls.file = File.objects.create(file=cls.image, processed=False)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        time.sleep(1)
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
