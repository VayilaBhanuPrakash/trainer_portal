from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TrainerRegistrationForm,TrainerLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from students.models import Student

def register_view(request):

    if request.method == 'POST':
        form = TrainerRegistrationForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            return redirect('login')

    else:
        form = TrainerRegistrationForm()

    context = {
        'form' : form
    }

    return render(request,'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = TrainerLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid email or password.")
            
    else:
        form = TrainerLoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required(login_url='login')
def home_view(request):

    total_students = Student.objects.filter(trainer=request.user).count()
    context = {
        'total_students': total_students
    }
    return render(request, 'accounts/home.html',context)

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def logout_confirm_view(request):
    return render(request, 'accounts/logout_confirm.html')
