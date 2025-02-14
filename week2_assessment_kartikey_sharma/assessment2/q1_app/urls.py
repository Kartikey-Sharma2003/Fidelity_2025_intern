from django.contrib import admin
from django.urls import path,include
from .views import ProductViewSet

urlpatterns = [
    path('list/', ProductViewSet.as_view({'get': 'list'})),
    path('create/', ProductViewSet.as_view({'post': 'create'})),
    path('retreive/<int:pk>/', ProductViewSet.as_view({'get': 'retreive'})),
    path('update/<int:pk>/', ProductViewSet.as_view({'put': 'update'})),
    path('delete/<int:pk>/', ProductViewSet.as_view({'delete': 'destroy'})),
    
]

