# from rest_framework import serializers
# from .models import Trip

# class TripSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trip
#         fields = ['trip_id', 'trip_name', 'trip_date', 'trip_time', 'trip_cost', 'trip_description', 'trip_location']
from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['start_location', 'end_location', 'trip_duration']  # Only required fields
