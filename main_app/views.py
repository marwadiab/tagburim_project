from django.shortcuts import render

# main page
def home(request):
    return render(request, 'home.html')
from django.shortcuts import render

def student_page(request):
    return render(request, 'student.html')

def teacher_page(request):
    return render(request, 'teacher.html')

def admin_page(request):
    return render(request, 'Dean of Student office.html')

#Student page
def request_privet(request):
    return render(request, 'request_privet.html')

def cancel_privet(request):
    return render(request, 'cancel_privet.html')

def response(request):
    return render(request, 'response.html')

def request_group(request):
    return render(request, 'request_group.html')

def cancel_group(request):
    return render(request, 'cancel_group.html')

def system(request):
    return render(request, 'system.html')
