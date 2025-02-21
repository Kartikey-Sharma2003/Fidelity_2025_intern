from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ItemDetailView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]