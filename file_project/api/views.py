from rest_framework.generics import CreateAPIView, ListAPIView

from api.models import File
from api.serializers import FileSerializer


class CreateFileAPIView(CreateAPIView):
    http_method_names = ('post',)
    queryset = File.objects.all()
    serializer_class = FileSerializer


class ListFileAPIView(ListAPIView):
    http_method_names = ('get',)
    queryset = File.objects.all()
    serializer_class = FileSerializer
