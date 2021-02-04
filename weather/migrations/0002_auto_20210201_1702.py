# Generated by Django 3.1.5 on 2021-02-01 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='humidity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='weather',
            name='precipitation_probability',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.IntegerField(help_text='Temperature in ºC', validators=[django.core.validators.MinValueValidator(-50), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='weather',
            name='visibility',
            field=models.FloatField(help_text='Visibility in km', validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(30.0)]),
        ),
    ]
