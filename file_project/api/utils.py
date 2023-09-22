from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def create_image() -> SimpleUploadedFile:
    width = 1000
    height = 500

    image = Image.new("RGB", (width, height))

    image_path = "test_image.jpeg"
    image.save(image_path, "JPEG")

    with open(image_path, "rb") as f:
        image_content = f.read()

    image = SimpleUploadedFile(
        "test_image.jpeg",
        image_content,
        content_type="image/jpeg"
    )

    return image
