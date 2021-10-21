from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('register/', patient_register, name='patient-register'),
    path('login/', LoginView.as_view(template_name='patient/login.html'),
         name='patient-login'),
    path('dashboard/', patient_dashboard, name='patient-dashboard')
]