from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("login_page/", views.login_page, name="login_page"),
    path("signup/", views.signup, name="signup"),
    path("forgotpassword/", views.forgotpassword, name='forgotpassword'),
    path("employees/", views.employees, name='employees'),
]