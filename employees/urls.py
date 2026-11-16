from django.urls import path
from . import views

urlpatterns = [
    path('<int:Emp_id>/',views.employee_detail, name= 'employee_detail'),
]