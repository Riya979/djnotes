from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Employee
# Create your views here.
class EmployeeCreate(CreateView):
    model=Employee
    fields='__all__'
    template_name='employee_form.html'
    success_url='/list'
    
class EmployeeListview(ListView):
    template_name='employee_list.html'
    model=Employee
    def get_queryset(self):
        qs=Employee.objects.all()
        return qs
class EmployeeUpdateView(UpdateView):
    model=Employee
    fields='__all__'
    template_name='employee_form.html'
    success_url='/list'
class EmployeeDeleteView(DeleteView):
    model=Employee
    fields='__all__'
    template_name='employee_form.html'
    success_url='/list'