from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Employee, Position, Contact
from .forms import EmployeeForm, ContactForm

def employee_list(request):
	employees = Employee.objects.all()
	return render(request, 'employee_list.html', {'employees':employees})


def employee_form(request):
	form = EmployeeForm()

	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Employee was created successfully')
			return redirect('employee_list')

	context = {'form': form}
	return render(request, 'employee_form.html', context)


def employee_update(request, id):
	employees = Employee.objects.get(id=id)
	form = EmployeeForm(instance=employees)

	if request.method == 'POST':
		form = EmployeeForm(request.POST, instance=employees)
		if form.is_valid():
			form.save()
			messages.success(request, 'Employee was updated successfully')
			return redirect('employee_list')

	context = {'form': form}
	return render(request, 'employee_form.html', context)

def employee_delete(request, id):
	employees = Employee.objects.get(id=id)
	employees.delete()
	messages.warning(request, 'Employee was deleted successfully')
	return redirect('employee_list')


def contact(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Message was sent successfully')
			return redirect('employee_list')

	context = {'form': form}
	return render(request, 'contact.html', context)