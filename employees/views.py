from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from employees.models import Employee

def employee_detail(request, Emp_id):
    employee=get_object_or_404(Employee,Employee_id=Emp_id)
    context = {
        'employee' : employee
    }
    return render(request,'employee_detail.html', context)

# Create your views here.
