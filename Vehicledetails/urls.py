"""Vehicledetails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud.views import VehicleListView,VehicleUpdateView,RegistrationView,LoginView,VehicleCreateView,VehicleDeleteView,signout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("vehicle_list/",VehicleListView.as_view(),name="list"),
    path("vehicle/update/<int:id>/",VehicleUpdateView.as_view(),name="update"),
    path("vehicle/create/",VehicleCreateView.as_view(),name="create"),
    path("vehicle/remove/<int:id>/",VehicleDeleteView.as_view(),name="remove"),
    path("accounts/register/",RegistrationView.as_view(),name='register'),
    path('',LoginView.as_view(),name="signin"),
    path("signout/",signout_view,name="logout")
]
