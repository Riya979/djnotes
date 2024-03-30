from django.shortcuts import render,redirect
from .models import StudentData1

# Create your views here.
def home(request):
    sd=StudentData1.objects.all()
    return render(request,'home.html',{'sd':sd})
def add_student(request):
    if request.method=='GET':
        return render(request,'student_reg.html')
    else:
        StudentData1(
            firstname=request.POST.get('fname'),
            lastname=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            marks1=request.POST.get('marks1'),
            marks2=request.POST.get('marks2'),
            marks3=request.POST.get('marks3'),
            marks4=request.POST.get('marks4')
            ).save()
        sd=StudentData1.objects.all()
        return render(request,'home.html',{'sd':sd})
    
def update_data(request,id):
    sd=StudentData1.objects.get(id=id)
    return render(request,'update_data.html',{'sd':sd})
    
def save_data(request,id):
    sd=StudentData1.objects.get(id=id)
    sd.firstname=request.POST.get('fname')
    sd.lastname=request.POST.get('lname')
    sd.email=request.POST.get('email')
    sd.mobile=request.POST.get('mobile')
    sd.marks1=request.POST.get('marks1')
    sd.marks2=request.POST.get('marks2')
    sd.marks3=request.POST.get('marks3')
    sd.marks4=request.POST.get('marks4')
    sd.save()
    return redirect(home)

def delete_data(request,id):
    sd=StudentData1.objects.get(id=id)
    sd.delete()
    return redirect(home)