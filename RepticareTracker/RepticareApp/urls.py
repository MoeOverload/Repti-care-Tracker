from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReptiCareApp, name="ReptiCareApp"),
    path("Login/", views.Login, name="Login"),
    path("signup/", views.createUser, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/",views.dashboard, name="dashboard"),
    path("reptiles/add/", views.add_reptile, name="add_reptile"),
    path("reptile/delete/<int:reptile_id>/", views.delete_reptile, name="delete_reptile"),
    path("terrariums/add/", views.add_terrarium, name="add_terrarium"),
    path("terrarium/delete/<int:terrarium_id>/" ,views.delete_terrarium, name="delete_terrarium"),
 ]