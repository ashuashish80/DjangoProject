from django.shortcuts import render

# Create your views here.

def calculate(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        operation = request.POST.get('operation')
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        return render(request, 'calculator.html', {'result': result})
    else:
        return render(request, 'calculator.html')
