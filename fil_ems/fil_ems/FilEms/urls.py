from django.urls import path
from .views import register_employee, login_employee, logout_employee, dashboard, create_employee, employee_list, update_employee, delete_employee

urlpatterns = [
    path('register/', register_employee, name='register'),
    path('login/', login_employee, name='login'),
    path('logout/', logout_employee, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_employee, name='create_employee'),
    path('list/', employee_list, name='employee_list'),
    path('update/<str:emp_id>/', update_employee, name='update_employee'),
    path('delete/<str:emp_id>/', delete_employee, name='delete_employee'),
]