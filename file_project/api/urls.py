from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register('file', views.FileViewSet)

urlpatterns = [
    # path('upload/', views.FileViewSet.as_view(), name=''),
    # path('files/', views.Files.as_view(), name=''),
    path('', include(router.urls)),
]
