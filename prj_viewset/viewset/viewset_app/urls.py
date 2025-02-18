from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from viewset_app.views import CustomerViewSet
routers = routers.DefaultRouter()
routers.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns=[
   path('', include(routers.urls))

]