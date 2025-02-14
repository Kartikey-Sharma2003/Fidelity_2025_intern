from django.contrib import messages
from django.contrib.auth import logout
from .forms import EmployeeRegisterForm, EmployeeLoginForm, EmployeeForm
from .models import Employee
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def register_employee(request):
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_employee(request):
    if request.method == "POST":
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data['emp_id']
            date_of_joining = form.cleaned_data['date_of_joining']

            try:
                employee = Employee.objects.get(emp_id=emp_id, date_of_joining=date_of_joining)
                request.session['employee_id'] = employee.emp_id  
                messages.success(request, f"Welcome, {employee.name}!")
                return redirect('dashboard')
            except Employee.DoesNotExist:
                messages.error(request, "Invalid Employee ID or Date of Joining!")

    else:
        form = EmployeeLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_employee(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

def dashboard(request):
    emp_id = request.session.get('employee_id')
    if not emp_id:
        return redirect('login')

    employee = Employee.objects.get(emp_id=emp_id)
    return render(request, 'dashboard.html', {'employee': employee})


def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully!")
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def update_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})