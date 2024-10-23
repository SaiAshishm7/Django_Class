from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def insertData(request):
    name = request.POST['name']    # Changed from nameVar
    rollno = request.POST['rollno']  # Changed from ageVar to rollno
    
    Student.objects.create(name=name, rollno=rollno)  # Changed from Customer to Student
    students = Student.objects.all()  # Get all student records
    return render(request, 'home.html', {'students': students})