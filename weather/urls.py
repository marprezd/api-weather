# api-weather/weather/urls.py
from rest_framework import routers
from .views import WeatherViewSet

router = routers.DefaultRouter()
# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')
router.register('weather', WeatherViewSet, 'weather')
urlpatterns = router.urls
