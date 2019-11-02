from django.db import models

class Launch(models.Model):
    launch_year = models.IntegerField()
    launch_date = models.DateField()
    rocket_name = models.CharField(max_length=100)
    land_success = models.BooleanField()
    nationality = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    launch_success = models.BooleanField()