from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud_app.forms import OrderForm
from crud_app.models import Orders
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def orderformview(request):
    form=OrderForm()
    if(request.method)=='POST':
        form=OrderForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("Data saved")
    return render(request,'order.html',{'order':form})    

def showorder(request):
    orders=Orders.objects.all()
    return render(request,'showorder.html',{'ord':orders})

def updateord(request,ordid):
    obj=Orders.objects.get(ordId=ordid)
    form=OrderForm(instance=obj)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse("Data updated")
    return render(request,'order.html',{'order':form})

def deleteord(request,ordid):
    try:
        obj=Orders.objects.get(ordId=ordid)
        obj.delete()
        return HttpResponse("Data deleted")
    except Orders.DoesNotExist:
        return HttpResponse("Data not found")

def setsession(request):
    request.session['name']='kartikey'
    return HttpResponse("session is set")

def getsession(request):
    name=request.session['name']
    return HttpResponse(name)

def showstatic(request):
    return render(request,'staticfile.html')

def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=uname).exists():
            messages.error(request, 'username does not exist')
        else:
            user = authenticate(request, username=uname, password=password)
            if user is None:
                messages.error(request, 'username or password is incorrect')
            else:
                auth_login(request, user)
                return redirect('home')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=uname, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')