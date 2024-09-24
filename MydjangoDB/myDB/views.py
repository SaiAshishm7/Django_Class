from django.shortcuts import render,redirect, get_object_or_404
from .models import Customer


def home(request):
    return render(request,'home.html')

def insertData(request):
    n=request.POST['nameVar']
    a=request.POST['ageVar']
    Customer.objects.create(name=n, age=a);
    customers=Customer.objects.all()
    return render(request,'home.html',{'customers':customers})

# myapp/views.py
def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()  # Deletes the selected customer
    return redirect('customerList')


