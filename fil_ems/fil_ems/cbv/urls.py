from django.contrib import admin
from django.urls import path,include
from django.views.generic import CreateView
from cbv.views import Myclass,ProductCreate,ProductUpdate,ProductDelete,ProductList,BaseView,HomeView
from . import views

app_name = 'cbv'
urlpatterns = [
    path('cbv/', Myclass.as_view()),
     path('create/', ProductCreate.as_view(), name='cbv_create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='cbv_update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='cbv_delete'),
     path('list/', ProductList.as_view(), name='product_list'),
     path('base/', BaseView.as_view(), name = 'base'),
    path('home/', HomeView.as_view(), name = 'home'),
]
