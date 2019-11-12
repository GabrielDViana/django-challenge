# from django.shortcuts import render
# from django.conf import settings
from rest_framework.generics import ListAPIView, RetrieveAPIView
# import requests

from launch.models import Launch
from .serializers import LaunchSerializer

class LaunchesListView(ListAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer

class LaunchDetailView(RetrieveAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer

# def save_embed(request):

#     if request.method == "POST":
#         r = requests.get('https://api.spacexdata.com/v3/launches')
#         json = r.json()
#         serializer = LaunchSerializer(data=json)
#         if serializer.is_valid():
#             embed = serializer.save()
