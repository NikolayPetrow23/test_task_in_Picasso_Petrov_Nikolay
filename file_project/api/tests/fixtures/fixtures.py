import shutil
import tempfile

from PIL import Image
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from rest_framework.test import APITestCase

from api.utils import create_image

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
NUMBER_OF_OBJECT_FILE = 3
LAST_ITEM_FILE = 4


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class FileProjectAPITest(APITestCase):
    fixtures = ['files.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.image = create_image()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
