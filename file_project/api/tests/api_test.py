import os

from django.urls import reverse
from rest_framework import status

from api.models import File
from api.tests.fixtures.fixtures import (
    FileProjectAPITest,
    LAST_ITEM_FILE,
    NUMBER_OF_OBJECT_FILE
)


class FileAPITest(FileProjectAPITest):
    def test_create_file(self):
        url = reverse('api:upload')
        with open(self.image_path, 'rb') as image_file:
            response = self.client.post(
                url,
                {'file': image_file},
                format='multipart'
            )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(File.objects.count(), NUMBER_OF_OBJECT_FILE + 1)
        self.assertEqual(
            os.path.basename(
                File.objects.get(pk=LAST_ITEM_FILE).file.name
            ),
            self.name_images
        )
        print(type(File.objects.get(pk=LAST_ITEM_FILE)))

    def test_list_file(self):
        url = reverse('api:files_list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) == NUMBER_OF_OBJECT_FILE)
