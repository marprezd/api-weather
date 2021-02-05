# api-weather/weather/tests/tests.py
from .factories import CustomUserFactory, WeatherFactory
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse


class TestWeatherApiViews(APITestCase):
    def setUp(self) -> None:
        self.forecast = WeatherFactory()
        self.user = CustomUserFactory()
        self.client = APIClient()
        
    def test_string_representation(self):
        forecast = WeatherFactory()
        self.assertEqual(
            'Weather forecast for {}'.format(forecast.city), str(forecast)
        )
            
    def test_if_any_user_has_permissions_to_read_posts(self):
        self.client.login(username='testuser1', password='userpass123')
        response = self.client.get(reverse('weather-detail', args=[str(self.forecast.id)]))
        self.assertEqual(response.status_code, 200)
        
    def test_if_an_user_can_only_edit_or_delete_their_posts(self):
        self.client.login(username='testuser1', password='userpass123')
        response = self.client.put(reverse('weather-detail', args=[str(self.forecast.id)]))
        self.assertTrue(response.status_code, 403)