from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'home.html')

def calculator(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operator = request.POST.get('operator')
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        
        # Format the result to display up to 4 decimal places if it's a float
        if isinstance(result, float):
            result = f"{result:.4f}".rstrip('0').rstrip('.')
    
    return render(request, 'calculator.html', {'result': result})