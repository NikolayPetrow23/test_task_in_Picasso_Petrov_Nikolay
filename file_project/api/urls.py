from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('upload/', views.CreateFileAPIView.as_view(), name='upload'),
    path('files/', views.ListFileAPIView.as_view(), name='files_list')
]
