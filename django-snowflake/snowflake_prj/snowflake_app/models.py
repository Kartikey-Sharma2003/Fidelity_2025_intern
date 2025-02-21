# from django.db import models

# class Trip(models.Model):
#     trip_id = models.AutoField(primary_key=True)
#     trip_name = models.CharField(max_length=100)
#     trip_date = models.DateField()
#     trip_time = models.TimeField()
#     trip_cost = models.DecimalField(max_digits=10, decimal_places=2)
#     trip_description = models.TextField()
#     trip_location = models.CharField(max_length=100)

#     def _str_(self):
#         return self.trip_name
from django.db import models

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    start_location = models.CharField(max_length=100)  # Start point of the trip
    end_location = models.CharField(max_length=100)  # Destination point
    trip_duration = models.IntegerField(default=60)  # Duration in minutes/hours
    trip_date = models.DateField()
    trip_time = models.TimeField()
    trip_cost = models.DecimalField(max_digits=10, decimal_places=2)


