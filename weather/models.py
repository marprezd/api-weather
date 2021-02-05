# api-weather/weather/models.py
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
           

class Weather(models.Model):
    class WindDirection(models.TextChoices):
        NONE = "undefined", "Undefined",
        NORTH = "n", "N",
        NORTH_EAST = "ne", "NE",
        EAST = "e", "E",
        SOUTH_EAST = "se", "SE",
        SOUTH = "s", "S",
        SOUTH_WEST = "sw", "SW",
        WEST = "w", "W",
        NORTH_WEST = "nw", "NW"
        
        
    class TypesPrecipitation(models.TextChoices):
        NONE = "undefined", "Undefined",
        RAIN = "rain", "Rain",
        DRIZZLE = "drizzle", "Drizzle",
        SNOW = "snow", "Snow",
        HAIL = "hail", "Hail"


    class Cloudiness(models.TextChoices):
        NONE = "undefined", "Undefined",
        CLEAR = "clear", "Clear",
        MOSTLY_CLEAR = "mostly_clear", "Mostly Clear",
        PARTLY_CLOUDY = "partly_cloudy", "Partly Cloudy",
        MOSTLY_CLOUDY = "mostly_cloudy", "Mostly Cloudy",
        CLOUDY = "cloudy", "Cloudy",
        
    city = models.CharField(max_length=50, help_text='Use the capitalize format, e.g: Madrid')
    country = models.CharField(max_length=50, help_text='Use the capitalize format, e.g: Spain')
    temperature = models.IntegerField(help_text='Temperature in ºC', 
                                      validators=[MinValueValidator(-50), MaxValueValidator(50)])
    atmospheric_pressure = models.FloatField(help_text='Atmospheric pressure in mbar')
    wind_sped = models.PositiveIntegerField(help_text='Wind speed in km/h')
    wind_direction = models.CharField("Wind direction",
                                      max_length=9,
                                      choices=WindDirection.choices,
                                      default=WindDirection.NONE)
    humidity = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)])
    precipitation_probability = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)])
    types_precipitation = models.CharField("Types of Precipitation",
                                           max_length=9,
                                           choices=TypesPrecipitation.choices,
                                           default=TypesPrecipitation.NONE)
    cloudiness = models.CharField("Cloudiness",
                                  max_length=13,
                                  choices=Cloudiness.choices,
                                  default=Cloudiness.NONE)
    visibility = models.FloatField(help_text='Visibility in km', 
                                   validators=[MinValueValidator(1.0), MaxValueValidator(30.0)])
    date = models.DateTimeField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "Weather forecast for {}".format(self.city)
    