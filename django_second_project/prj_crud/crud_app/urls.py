from django.urls import path
from . import views
urlpatterns = [
    path('order/', views.orderformview),
    path('show/',views.showorder),
    path('update/<int:ordid>/',views.updateord,name='updateurl'),
    path('delete/<int:ordid>/',views.deleteord),
    path('setseeion/',views.setsession),
    path('getsession/',views.getsession),
    path('static/',views.showstatic),
    path('login/',views.user_login),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
]