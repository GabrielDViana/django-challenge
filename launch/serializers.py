from rest_framework import serializers
from launch.models import Launch

class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = '__all__'