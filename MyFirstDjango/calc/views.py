from django.shortcuts import render

def home(request):
    return render (request,'home.html',{'name':'cyrus'})

# Create your views here.
