
from django.shortcuts import  get_object_or_404,render
from salary.models import Employee

def employee_detail(request,pk):
    employees=get_object_or_404(Employee,pk=pk)
    context={
        'employees':employees,
    }
    return render(request,'employee_detail.html',context)
