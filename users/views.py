from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")

            login(request, user)
            
            return redirect("profile") 

    else:
        form = UserRegistrationForm()
    
    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "users/profile.html", {"profile": profile})