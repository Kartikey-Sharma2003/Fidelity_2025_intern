from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id','e_fname','e_lname','salary','doj']
    
# Register your models here.
