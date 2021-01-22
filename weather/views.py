# api-weather/weather/views.py
from rest_framework import viewsets
from .serializers import WeatherSerializer
from .models import Weather
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthorOrReadOnly]
