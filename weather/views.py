# api-weather/weather/views.py
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters import CharFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import WeatherSerializer
from .models import Weather
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class WeatherFilter(filters.FilterSet):
    city = CharFilter(field_name='city', lookup_expr='icontains')
    country = CharFilter(field_name='country', lookup_expr='icontains') 
    class Meta:
        model = Weather
        fields = ['city', 'country']


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_class = WeatherFilter
    search_fields = ('^city', '^country')
    ordering_fields = ('city',)
