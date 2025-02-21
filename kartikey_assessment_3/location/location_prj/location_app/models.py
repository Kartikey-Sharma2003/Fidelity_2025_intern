from django.db import models

class Location(models.Model):
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10, unique=True)
    state = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, default='India')

    def _str_(self):
        return f"{self.district}, {self.state} ({self.pincode})"