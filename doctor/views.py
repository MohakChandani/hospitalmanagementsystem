from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import DoctorUserForm, DoctorForm
from django.http import HttpResponseRedirect

# Create your views here.


def doctor_register(request):
    user_form = DoctorUserForm()
    doctor_form = DoctorForm()
    view_context = {'user_form': user_form, 'doctor_form': doctor_form}

    if request.method == 'POST':
        user_form = DoctorUserForm(request.POST)
        doctor_form = DoctorForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            doctor = doctor_form.save(commit=False)
            doctor.user = user
            doctor.save()

            # Adding doctor to the DOCTOR group
            doctor_group = Group.objects.get_or_create(name='DOCTOR')
            doctor_group[0].user_set.add(user)

        return HttpResponseRedirect('/doctor/login')
    return render(request, 'doctor/register.html', context=view_context)


# Doctor's dashboard
@login_required(login_url='doctor-login')
def doctor_dashboard(request):
    return render(request, 'doctor/dashboard.html')