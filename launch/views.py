# from django.shortcuts import render
# from django.conf import settings
import requests
import json as JSON

from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http import HttpResponse, JsonResponse

from launch.models import Launch
from .serializers import LaunchSerializer


class LaunchesListView(ListAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer

class LaunchDetailView(RetrieveAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer

def upcoming(request):

    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
        json = r.json()
        launch = Launch()
        launch.flight_number = int(json[0]['flight_number'])
        launch.launch_year = int(json[0]['launch_year'])
        launch.launch_date_utc = json[0]['launch_date_utc']
        launch.launch_date_local = json[0]['launch_date_local']
        launch.rocket_id = json[0]['rocket']['rocket_id']
        launch.rocket_name = json[0]['rocket']['rocket_name']
        launch.rocket_type = json[0]['rocket']['rocket_type']
        launch.land_success = False
        launch.site_name = json[0]['launch_site']['site_name_long']
        launch.customer = json[0]['rocket']['second_stage']['payloads'][0]['customers'][0]
        launch.nationality = json[0]['rocket']['second_stage']['payloads'][0]['nationality']
        launch.manufacturer = json[0]['rocket']['second_stage']['payloads'][0]['manufacturer']
        launch.launch_success = False

        serializer = LaunchSerializer(data=launch.as_json())

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
