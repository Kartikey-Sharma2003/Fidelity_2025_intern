from django.shortcuts import render
from django.http import HttpResponse
def index(reqquest):
    return HttpResponse("hello from my app")

# Create your views here.
