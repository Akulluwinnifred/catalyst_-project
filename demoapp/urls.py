from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("login_page/", views.login_page, name="login_page"),
    path("signup/", views.signup, name="signup"),
    path("forgotpassword/", views.forgotpassword, name='forgotpassword'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("babies_reg/", views.babies_reg, name='babies_reg'),
    path("sitters_reg/", views.sitters_reg, name= 'sitters_reg'),
    path("baby_attendance/", views.baby_attendance, name='baby_attendance'),
    path("sitter_attendance/", views.sitter_attendance, name= "sitter_attendance"),
    path("payments/", views.payments, name='payments')
]