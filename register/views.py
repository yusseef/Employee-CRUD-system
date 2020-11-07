from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def employee_list(request):
    context = {"employee_list":Employee.objects.all()}
    return render(request, 'list.html', context)

def employee_form(request,id=0):
    if request.method =='GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request, 'form.html', {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')

