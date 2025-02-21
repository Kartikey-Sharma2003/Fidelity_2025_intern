from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Location
from .serializers import BasicLocationSerializer, LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationByPincodeView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'pincode'

    def get(self, request, *args, **kwargs):
        pincode = self.kwargs.get('pincode')
        try:
            location = Location.objects.get(pincode=pincode)
            data = {
                "pincode": location.pincode,
                "district": location.district,
                "state": location.state,
                "latitude": location.latitude,
                "longitude": location.longitude,
                "city": location.city,
                "country": location.country,
            }
            return Response(data)
        except Location.DoesNotExist:
            return Response({"error": "Location not found"}, status=404)
        
class BasicLocationView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = BasicLocationSerializer