from django.shortcuts import render
from .forms import BMICalculatorForm
from .models import BMIRecord

def home(request):
    return render(request, 'home.html')

def calculate_bmi(request):
    result = None
    category = None
    
    if request.method == 'POST':
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            
            bmi_record = BMIRecord(height=height, weight=weight)
            bmi = bmi_record.calculate_bmi()
            bmi_record.save()
            
            if bmi < 18.5:
                category = 'Underweight'
            elif 18.5 <= bmi < 25:
                category = 'Normal weight'
            elif 25 <= bmi < 30:
                category = 'Overweight'
            else:
                category = 'Obese'
                
            result = {
                'bmi': bmi,
                'category': category
            }
    else:
        form = BMICalculatorForm()
    
    return render(request, 'calculate.html', {
        'form': form,
        'result': result,
        'category': category
    })