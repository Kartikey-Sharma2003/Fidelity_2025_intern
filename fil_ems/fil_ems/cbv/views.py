from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from cbv.models import Product
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db import models
class Myclass(View):
    def get(self, request):
        return HttpResponse("Views form class")
    
class ProductCreate(CreateView):
    model = Product
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('cbv:cbv_create')


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cbv:cbv_update', kwargs={'pk': self.object.pk})

class ProductDelete(DeleteView):
    model = Product
    template_name = 'create.html'  
    success_url = reverse_lazy('cbv:product_list')

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html' 
    context_object_name = 'products'

class BaseView(TemplateView):
    template_name = 'base.html'

class HomeView(TemplateView):
    template_name = 'home.html'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
# Create your views here.
