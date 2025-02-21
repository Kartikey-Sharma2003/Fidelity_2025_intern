# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TripViewSet

# router = DefaultRouter()
# router.register(r'trips', TripViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TripListCreateView, TripDetailView

router = DefaultRouter()

urlpatterns = [
    path('trips/', TripListCreateView.as_view(), name='trip-list'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
]

urlpatterns += router.urls
