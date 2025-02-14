from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('setsession/', views.set_session),
    path('getsession/', views.get_session),
]
