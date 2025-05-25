from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User

def login_page(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page
        else:
            error = "Invalid credentials"

    return render(request, "accounts/login.html", {"error": error})

def home(request):
    return render(request, "accounts/home.html")
