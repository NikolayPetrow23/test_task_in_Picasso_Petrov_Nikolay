from rest_framework.generics import CreateAPIView, ListAPIView

from api.models import File
from api.serializers import FileSerializer


class CreateFileAPIView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class ListFileAPIView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
