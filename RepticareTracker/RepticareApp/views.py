from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Reptile, Terrarium
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
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
    profile = Profile.objects.get(user=request.user)
    reptiles = profile.reptiles.all() 
    terrariums = profile.terrariums.all()
    return render(request,"dashboard/index.html",{
        "profile":profile,
        "reptiles": reptiles,
        "terrariums": terrariums,
        
    })


def add_reptile(request):
    
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)
    owner = Profile.objects.get(user=request.user)
    reptile_name = request.POST.get("reptile_name")
    reptile_species = request.POST.get("reptile_species")
    estimated_age_months = request.POST.get("estimated_age_months")
    
    if not reptile_name or not reptile_species :
         return JsonResponse({
            "success": False,
            "message": "missing fields"
            }, status=400)
    try:
        estimated_age_months = int(estimated_age_months) if estimated_age_months else None
    except ValueError:
        return JsonResponse({
            "success": False,
            "message": "Age must be a number"
        }, status=400)
    Reptile.objects.create(
        reptile_name = reptile_name,
        owner = owner,
        reptile_species = reptile_species,
        estimated_age_months = estimated_age_months,
        estimated_age_record_date = now().date()
    )
    
    return JsonResponse({"success": True})
        
def delete_reptile(request,reptile_id):
    if request.method != "POST":
        return JsonResponse({"success": False}, status=400)
    reptile = get_object_or_404(
        Reptile,
        id=reptile_id,
        owner__user = request.user
    )
    reptile.delete()
    return JsonResponse({"success":True})

def add_terrarium(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)
    owner = Profile.objects.get(user=request.user)
    reptile_id = request.POST.get("reptile_id")
    terrarium_nickname = request.POST.get("terrarium_nickname")
    if not terrarium_nickname or not reptile_id:
         return JsonResponse({
            "success": False,
            "message": "missing fields"
            }, status=400)
    reptile = get_object_or_404(Reptile, id=reptile_id,owner=owner)
    Terrarium.objects.create(
        owner = owner,
        reptile = reptile,
        terrarium_nickname = terrarium_nickname
    )
    return JsonResponse({"success": True})

def delete_terrarium(request,terrarium_id):
    if request.method != "POST":
        return JsonResponse({"success": False}, status=400)
    terrarium = get_object_or_404(
        Terrarium,
        id=terrarium_id,
        owner__user = request.user
    )
    terrarium.delete()
    return JsonResponse({"success":True})
