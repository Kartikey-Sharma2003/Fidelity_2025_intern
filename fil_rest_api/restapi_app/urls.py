from django.urls import path
from . import views

urlpatterns = [
    path('api/getdata/', views.getdata, name='getdata'),
]