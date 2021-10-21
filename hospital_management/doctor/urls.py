from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('register/', doctor_register, name='doctor-register'),
    path('login/', LoginView.as_view(template_name='doctor/login.html'),
         name='doctor-login'),
    path('dashboard/', doctor_dashboard, name='doctor-dashboard')
]