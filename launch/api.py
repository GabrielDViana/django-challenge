from launch.models import Launch
from rest_framework import viewsets, permissions
from .serializers import LaunchSerializer

class LaunchViewSet(viewsets.ModelViewSet):
    queryset = Launch.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LaunchSerializer