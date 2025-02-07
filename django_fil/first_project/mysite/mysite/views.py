from django.http import HttpResponse
from django.shortcuts import render
import requests

def home(request):
    return render(request,'home.html')
    # return HttpResponse("<h1>hello home</h1>")
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def mydata(request):
    data=[10,20,30,49]
    var='kartikey'
    course = ['python','java','scala','go','php']
    return render(request,'mydata.html',{'mydata':data,'var1':var,'course':course})
def my_view(request):
    res=requests.get('https://restcountries.com/v3.1/all')
    if res.status_code == 200:
        countries = res.json()
    else:
        countries = []
    return render(request,'home.html' , {'countries':countries})
def d_view(request,id):
    return render(request,'ddata.html',{'ddata':id})  


def student_task(request, id):
    data = {
        {
            'name': 'Shivam',
            'id': 101,
            'marks': [10, 20, 30, 40, 50]
        },
        {
            'name': 'Rahul',
            'id': 102,
            'marks': [10, 20, 30, 40, 50]
        },
        {
            'name': 'Rajat',
            'id': 103,
            'marks': [10, 20, 30, 40, 50]
        },
        {
            'name': 'Rohan',
            'id': 104,
            'marks': [10, 20, 30, 40, 50]
        },
        {
            'name': 'Kartik',
            'id': 105,
            'marks': [10, 20, 30, 40, 50]
        },
        {
            'name': 'Sunny',
            'id': 106,
            'marks': [10, 20, 30, 40, 50]
        },
        {
            'name': 'Tanish',
            'id': 107,
            'marks': [10, 20, 30, 40, 50]
        },
        {
            'name': 'Tushar',
            'id': 108,
            'marks': [10, 20, 30, 40, 50]
        }
    }

    # Find the student by ID
    student = next((item for item in data if item["id"] == id), None)

    if student:
        total_marks = sum(student['marks'])
        result = "Pass" if all(mark >= 15 for mark in student['marks']) else "Fail"
        student['total_marks'] = total_marks
        student['result'] = result

    return render(request, 'student.html', {'student': student})
