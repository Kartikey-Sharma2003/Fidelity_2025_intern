from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import ContactForm
def index(reqquest):
    return HttpResponse("hello from my app")
def form(request):
    print(request.POST)
    return render(request,"form.html")
def contactapp(request):
    if request.method=="post":
        form=ContactForm(request.POST)
        if(form.is_valid()):
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            print(name)
    else:
        form=ContactForm()        


    print(request.POST)
    return render(request,'contactapp.html',{'contactapp':form})
# Create your views here.
