from django.db import models


class Launch(models.Model):
    flight_number = models.IntegerField()
    launch_year = models.IntegerField()
    launch_date_utc = models.CharField(max_length=100)
    launch_date_local = models.CharField(max_length=100)
    rocket_id = models.CharField(max_length=100)
    rocket_name = models.CharField(max_length=100)
    rocket_type = models.CharField(max_length=100)
    land_success = models.BooleanField()
    site_name = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    launch_success = models.BooleanField()

    def as_json(self):
        return dict(
            flight_number=self.flight_number,
            launch_year=self.launch_year,
            launch_date_utc=self.launch_date_utc,
            launch_date_local=self.launch_date_local,
            rocket_id=self.rocket_id,
            rocket_name=self.rocket_name,
            rocket_type=self.rocket_type,
            land_success=self.land_success,
            site_name=self.site_name,
            customer=self.customer,
            nationality=self.nationality,
            manufacturer=self.manufacturer,
            launch_success=self.launch_success
        )
