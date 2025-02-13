from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                auth_login(request, user)  # Use auth_login to avoid conflict with the view function
                return redirect('profile')
            except IntegrityError:
                messages.error(request, "Username already exists. Please choose a different username.")
                return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):  # Renamed to avoid conflict with the import
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Use auth_login to avoid conflict with the view function
            messages.success(request, f'Welcome back, {username}!')
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'users/login.html')


def logout_view(request):
    auth_logout(request)  
    return redirect('register')   # Adjust 'register' to your desired redirect page


@login_required
def profile(request):
    return render(request, 'users/profile.html')  # Ensure you have a profile.html template
