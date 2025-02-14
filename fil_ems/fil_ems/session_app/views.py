from django.shortcuts import render
from django.http import HttpResponse
def set_session(request):
    request.session['name'] = 'kartikey'
    request.session.set_expiry(10)
    return HttpResponse("session created")
def get_session(request):
    name = request.session.get('name')
    return HttpResponse(f"session value is {name}")

    
# Create your views here.