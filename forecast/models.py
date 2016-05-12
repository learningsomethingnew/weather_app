from django.db import models

# Create your models here.
#   Current conditions at that location
#   10 day forecast for that location
#   Sunrise and sunset times
#   Any current weather alerts
#   A list of all active hurricanes (anywhere)


class UpdateManager(models.Model):
    api_request_time = models.DateTimeField()
    request_zip = models.IntegerField()


class CurrentConditions(models.Model):
    update_manager = models.ForeignKey(UpdateManager, on_delete=models.CASCADE)

    UV = models.CharField(max_length=10)
    feelslike_f = models.IntegerField()
    visibility_mi = models.IntegerField()
    temp_f = models.CharField(max_length=6)
    forecast_url = models.TextField()
    weather = models.CharField(max_length=200)
    relative_humidity = models.CharField(max_length=5)
    pressure_in = models.CharField(max_length=10)
    wind_dir = models.CharField(max_length=4)
    wind_string = models.CharField(max_length=100)
    wind_mph = models.FloatField()

class Forecast(models.Model):
    update_manager = models.ForeignKey(UpdateManager, on_delete=models.CASCADE)

    date_of_forecast = models.DateTimeField()

    # use simpleforecast
    day0_condition = models.TextField()
    day0_high = models.CharField(max_length=5)
    day0_low = models.CharField(max_length=5)
    day0_prob = models.CharField(max_length=5)
    day0_image = models.TextField()

    day1_condition = models.TextField()
    day1_high = models.CharField(max_length=5)
    day1_low = models.CharField(max_length=5)
    day1_prob = models.CharField(max_length=5)
    day1_image = models.TextField()

    day2_condition = models.TextField()
    day2_high = models.CharField(max_length=5)
    day2_low = models.CharField(max_length=5)
    day2_prob = models.CharField(max_length=5)
    day2_image = models.TextField()

    day3_condition = models.TextField()
    day3_high = models.CharField(max_length=5)
    day3_low = models.CharField(max_length=5)
    day3_prob = models.CharField(max_length=5)
    day3_image = models.TextField()

    day4_condition = models.TextField()
    day4_high = models.CharField(max_length=5)
    day4_low = models.CharField(max_length=5)
    day4_prob = models.CharField(max_length=5)
    day4_image = models.TextField()

    day5_condition = models.TextField()
    day5_high = models.CharField(max_length=5)
    day5_low = models.CharField(max_length=5)
    day5_prob = models.CharField(max_length=5)
    day5_image = models.TextField()


class Sun(models.Model):
    # astronomy
    update_manager = models.ForeignKey(UpdateManager, on_delete=models.CASCADE)
    # HH:MM
    sunrise = models.TimeField()
    sunset = models.TimeField()

class Alerts(models.Model):
    # alerts
    update_manager = models.ForeignKey(UpdateManager, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    message = models.TextField(blank=True)

