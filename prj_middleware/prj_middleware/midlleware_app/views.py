from django.shortcuts import render
from .models import Employee
from django.db.models import Sum
from django.db.models import Q

def get(request):
    queryset = Employee.objects.filter(Q(e_fname__startswith='k') | Q(e_lname__startswith='s'))
    print(queryset)
   
    
    return render(request, 'index.html', {'queryset':queryset})

    
# Create your views here.
