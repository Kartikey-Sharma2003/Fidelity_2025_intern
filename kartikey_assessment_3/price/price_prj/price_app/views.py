import requests
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        external_api_url = "http://127.0.0.1:8001/location/basic-locations/"
        try:
            response = requests.get(external_api_url)
            response.raise_for_status()
            external_data = response.json() 
        except requests.RequestException as e:
            external_data = {"error": str(e)}

        
        local_data = super().list(request, *args, **kwargs)

        return Response({
            "local_items": local_data.data,
            "external_items": external_data
        })

class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer