from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import (
    UserRegistrationForm,
    UserLoginForm
)

# login view
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    form = UserLoginForm()
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Wrong Credential!")
    
    return render(request, "login.html", {'form': form})



#registration view
def registration(request):
    form = UserRegistrationForm
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registration Successful")
            return redirect('login')
        
    context = {
        'form':form
    }
    return render(request, "registration.html", context)