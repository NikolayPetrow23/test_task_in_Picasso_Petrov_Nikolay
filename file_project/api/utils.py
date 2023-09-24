from api.models import File


def change_processed(pk: int):
    file = File.objects.get(pk=pk)
    file.processed = True
    file.save()


def check_type_file(file: File) -> str:
    file_type = file.file.name.split('.')[-1]
    return file_type
