from rest_framework.viewsets import ModelViewSet

from api.models import File
from api.serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = ('post', 'get',)
    # permission_classes = (ReadOnly,)
