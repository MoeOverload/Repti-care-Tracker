from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReptiCareApp, name="ReptiCareApp"),
    path("Login/", views.Login, name="Login"),
    path("signup/", views.createUser, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/",views.dashboard, name="dashboard")
 ]