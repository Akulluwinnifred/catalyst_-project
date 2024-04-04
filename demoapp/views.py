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


def dashboard(request):
    return render(request,"staff/dashboard.html")


def babies_reg(request):
    return render(request, 'staff/babies_reg.html')


def sitters_reg(request):
    return render(request, 'staff/sitters_reg.html')


def arrival(request):
    return  render(request, "staff/arrival.html")


def sitter_attendance(request):
    return render(request, 'staff/sitter_attendance.html')


def payments(request):
    return render(request, 'staff/payments.html')


def departure(request):
    return render(request, 'staff/departure.html')