from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, LocationByPincodeView, BasicLocationView

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('location/<str:pincode>/', LocationByPincodeView.as_view(), name='location-by-pincode'),
    path('basic-locations/', BasicLocationView.as_view(), name='basic-locations'),
]