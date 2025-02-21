from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('district', 'pincode', 'state', 'city', 'country', 'latitude', 'longitude')
    search_fields = ('pincode', 'district', 'state', 'city', 'country')