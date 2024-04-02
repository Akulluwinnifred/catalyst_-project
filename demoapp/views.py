from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html') 


def signup(request):
    return render(request,'signup.html')


def forgotpassword(request):
    return render(request,"forgotpassword.html")


def employees(request):
    return render(request,"staff/employees.html")