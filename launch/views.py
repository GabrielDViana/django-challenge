from django.shortcuts import render
from django.conf import settings

import requests

from .serializers import LaunchSerializer


def save_embed(request):

    if request.method == "POST":
        r = requests.get('https://api.spacexdata.com/v3/launches')
        json = r.json()
        serializer = LaunchSerializer(data=json)
        if serializer.is_valid():
            embed = serializer.save()