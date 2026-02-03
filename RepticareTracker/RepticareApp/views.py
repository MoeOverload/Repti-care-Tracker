from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
def ReptiCareApp(request):
    return render(request, "home/index.html")

def Login(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "login/index.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "login/index.html")

def createUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("signup_username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("login")
        if User.objects.filter(email = email).exists():
            messages.error(request, "user already exists")
            return redirect("login")
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password1
        )
        Profile.objects.create(user=user)
        login(request, user)
        return redirect("dashboard")
    return render(request, "login/index.html")


def logout_view(request):
    logout(request)
    return redirect("ReptiCareApp")


@login_required
def dashboard(request):
    return render(request,"dashboard/index.html")