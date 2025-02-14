from django import forms
from .models import Employee

class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'email', 'date_of_joining']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'})  
        }

class EmployeeLoginForm(forms.Form):
    emp_id = forms.CharField(label="Employee ID")
    date_of_joining = forms.DateField(label="Date of Joining", widget=forms.DateInput(attrs={'type': 'date'}))

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'email', 'date_of_joining']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'})  
        }