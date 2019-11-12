# from django.shortcuts import render
# from django.conf import settings
import requests

from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http import JsonResponse

from launch.models import Launch
from .serializers import LaunchSerializer


class LaunchesListView(ListAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


class LaunchDetailView(RetrieveAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


def next_launch(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/next')
        json = r.json()
        launch = Launch()
        launch.flight_number = int(json['flight_number'])
        launch.launch_year = int(json['launch_year'])
        launch.launch_date_utc = json['launch_date_utc']
        launch.launch_date_local = json['launch_date_local']
        launch.rocket_id = json['rocket']['rocket_id']
        launch.rocket_name = json['rocket']['rocket_name']
        launch.rocket_type = json['rocket']['rocket_type']
        launch.land_success = False
        launch.site_name = json['launch_site']['site_name_long']
        launch.customer = json['rocket']['second_stage']['payloads'][0]['customers'][0]
        launch.nationality = json['rocket']['second_stage']['payloads'][0]['nationality']
        launch.manufacturer = json['rocket']['second_stage']['payloads'][0]['manufacturer']
        launch.launch_success = False

        serializer = LaunchSerializer(data=launch.as_json())

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def latest_launch(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/latest')
        json = r.json()
        launch = Launch()
        launch.flight_number = int(json['flight_number'])
        launch.launch_year = int(json['launch_year'])
        launch.launch_date_utc = json['launch_date_utc']
        launch.launch_date_local = json['launch_date_local']
        launch.rocket_id = json['rocket']['rocket_id']
        launch.rocket_name = json['rocket']['rocket_name']
        launch.rocket_type = json['rocket']['rocket_type']
        launch.land_success = False
        launch.site_name = json['launch_site']['site_name_long']
        launch.customer = json['rocket']['second_stage']['payloads'][0]['customers']
        launch.nationality = json['rocket']['second_stage']['payloads'][0]['nationality']
        launch.manufacturer = json['rocket']['second_stage']['payloads'][0]['manufacturer']
        launch.launch_success = False

        serializer = LaunchSerializer(data=launch.as_json())

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def upcoming_launches(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
        json = r.json()

        launches = []

        for element in json:
            launch = Launch()
            launch.flight_number = int(element['flight_number'])
            launch.launch_year = int(element['launch_year'])
            launch.launch_date_utc = element['launch_date_utc']
            launch.launch_date_local = element['launch_date_local']
            launch.rocket_id = element['rocket']['rocket_id']
            launch.rocket_name = element['rocket']['rocket_name']
            launch.rocket_type = element['rocket']['rocket_type']
            launch.land_success = False
            launch.site_name = element['launch_site']['site_name_long']
            launch.customer = element['rocket']['second_stage']['payloads'][0]['customers']
            launch.nationality = element['rocket']['second_stage']['payloads'][0]['nationality']
            launch.manufacturer = element['rocket']['second_stage']['payloads'][0]['manufacturer']
            launch.launch_success = False

            launches.append(launch.as_json())
            serializer = LaunchSerializer(data=launch.as_json())
            if serializer.is_valid():
                serializer.save()

        return JsonResponse(launches, safe=False, status=201)


def past_launches(request):
    if request.method == "GET":
        r = requests.get('https://api.spacexdata.com/v3/launches/past')
        json = r.json()

        launches = []

        for element in json:
            launch = Launch()
            launch.flight_number = int(element['flight_number'])
            launch.launch_year = int(element['launch_year'])
            launch.launch_date_utc = element['launch_date_utc']
            launch.launch_date_local = element['launch_date_local']
            launch.rocket_id = element['rocket']['rocket_id']
            launch.rocket_name = element['rocket']['rocket_name']
            launch.rocket_type = element['rocket']['rocket_type']
            launch.land_success = False
            launch.site_name = element['launch_site']['site_name_long']
            launch.customer = element['rocket']['second_stage']['payloads'][0]['customers']
            launch.nationality = element['rocket']['second_stage']['payloads'][0]['nationality']
            launch.manufacturer = element['rocket']['second_stage']['payloads'][0]['manufacturer']
            launch.launch_success = False

            launches.append(launch.as_json())
            serializer = LaunchSerializer(data=launch.as_json())
            if serializer.is_valid():
                serializer.save()

        return JsonResponse(launches, safe=False, status=201)
