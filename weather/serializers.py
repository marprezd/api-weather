# api-weather/weather/serializers.py
from rest_framework import serializers
from .models import Weather
        

class WeatherSerializer(serializers.ModelSerializer):
    # Associate current user as post author
    # https://www.django-rest-framework.org/api-guide/validators/#currentuserdefault
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Weather
        fields = '__all__'


