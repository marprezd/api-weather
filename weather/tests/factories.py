# api-weather/weather/tests/factories.py
import datetime
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from factory import Faker, fuzzy, SubFactory, Sequence
from ..models import Weather


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
        
    username = Sequence(lambda n: 'username_{}'.format(n))
    email = Sequence(lambda n: "user{}@example.com".format(n))
    password = 'password'
    

class WeatherFactory(DjangoModelFactory):
    city = Faker('city')
    country = Faker('country')
    temperature = fuzzy.FuzzyInteger(-50, 50)
    atmospheric_pressure = fuzzy.FuzzyFloat(1020.0, 1030.0)
    wind_sped = fuzzy.FuzzyInteger(0, 400)
    wind_direction = fuzzy.FuzzyChoice(
        [x[0] for x in Weather.WindDirection.choices]
    )
    humidity = fuzzy.FuzzyInteger(1, 100)
    precipitation_probability = fuzzy.FuzzyInteger(1, 100)
    types_precipitation = fuzzy.FuzzyChoice(
        [x[0] for x in Weather.TypesPrecipitation.choices]
    )
    cloudiness = fuzzy.FuzzyChoice(
        [x[0] for x in Weather.Cloudiness.choices]
    )
    visibility = fuzzy.FuzzyFloat(1.0, 30.0)
    date = fuzzy.FuzzyDateTime(
        datetime.datetime(2021, 1, 1, tzinfo=datetime.timezone.utc),
        datetime.datetime(2022, 1, 1, tzinfo=datetime.timezone.utc),
    )
    author = SubFactory(CustomUserFactory)
    
    
    class Meta:
        model = Weather