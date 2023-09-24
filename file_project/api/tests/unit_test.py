import time

from PIL import Image

from api.tasks import process_image
from api.tests.fixtures.fixtures import FileUnitTestCase


class TaskTestCase(FileUnitTestCase):
    def test_process_pic(self):
        process_image.apply_async(
            args=[self.file.file.path, self.file.pk]
        )

        time.sleep(1)

        im = Image.open(self.file.file.path)
        self.assertEqual(im.size, (200, 100))
