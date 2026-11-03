from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TrainerRegistrationForm
from django.contrib.auth.models import User

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

            return redirect('register')

    else:
        form = TrainerRegistrationForm()

    context = {
        'form' : form
    }

    return render(request,'accounts/register.html', context)
