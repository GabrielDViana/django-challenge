from django.db import models


class Launch(models.Model):
    flight_id = models.CharField(max_length=100)
    start_end = models.DateField()
    flight_number = models.IntegerField()
    launch_year = models.IntegerField()
    launch_date_utc = models.DateField()
    launch_date_local = models.DateField()
    tbd = models.BooleanField()
    rocket_id = models.CharField(max_length=100)
    rocket_name = models.CharField(max_length=100)
    rocket_type = models.CharField(max_length=100)
    core_serial = models.CharField(max_length=100)
    land_success = models.BooleanField()
    landing_intent = models.BooleanField()
    landing_type = models.CharField(max_length=100)
    landing_vehicle = models.CharField(max_length=100)
    cap_serial = models.CharField(max_length=100)
    core_flight = models.IntegerField()
    block = models.IntegerField()
    gridfins = models.BooleanField()
    legs = models.BooleanField()
    core_reuse = models.BooleanField()
    capsule_reuse = models.BooleanField()
    fairings_reused = models.BooleanField()
    fairings_recovery_attempt = models.BooleanField()
    fairings_recovered = models.BooleanField()
    fairings_ship = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100)
    payload_id = models.CharField(max_length=100)
    norad_id = models.IntegerField()
    customer = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    payload_type = models.CharField(max_length=100)
    orbit = models.CharField(max_length=100)
    reference_system = models.CharField(max_length=100)
    regime = models.CharField(max_length=100)
    longitude = models.FloatField()
    semi_major_axis_km = models.FloatField()
    eccentricity = models.FloatField()
    periapsis_km = models.FloatField()
    apoapsis_km = models.FloatField()
    inclination_deg = models.FloatField()
    period_min = models.FloatField()
    lifespan_years = models.IntegerField()
    epoch = models.CharField(max_length=100)
    mean_motion = models.FloatField()
    raan = models.FloatField()
    launch_success = models.BooleanField()