# api-weather/weather/models.py
from django.db import models
from django.core.exceptions import ValidationError

# Custom validators
# https://docs.djangoproject.com/en/3.1/ref/validators/
def validate_temperature(value):
    if value < -98 or value > 60:
        raise ValidationError('%(value)s must be in the range [-98, 60]', params={'value': value},)  

def validate_visibility(value):
    if value < 0.0 or value > 100.0:
        raise ValidationError('%(value)s must be in the range [0.0, 100.0]', params={'value': value},)  
        
def validate_humidity_precipitation(value):
    if value > 100:
        raise ValidationError('%(value)s should not be greater than 100', params={'value': value},)  
           
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
    temperature = models.IntegerField(help_text='Temperature in ºC', validators=[validate_temperature])
    atmospheric_pressure = models.FloatField(help_text='Atmospheric pressure in mbar')
    wind_sped = models.PositiveIntegerField(help_text='Wind speed in km/h')
    wind_direction = models.CharField("Wind direction",
                                      max_length=9,
                                      choices=WindDirection.choices,
                                      default=WindDirection.NONE)
    humidity = models.PositiveIntegerField(validators=[validate_humidity_precipitation])
    precipitation_probability = models.PositiveIntegerField(validators=[validate_humidity_precipitation])
    types_precipitation = models.CharField("Types of Precipitation",
                                           max_length=9,
                                           choices=TypesPrecipitation.choices,
                                           default=TypesPrecipitation.NONE)
    cloudiness = models.CharField("Cloudiness",
                                  max_length=13,
                                  choices=Cloudiness.choices,
                                  default=Cloudiness.NONE)
    visibility = models.FloatField(help_text='Visibility in km', validators=[validate_visibility])
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.city
    