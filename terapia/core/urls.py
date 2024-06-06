from django.urls import path
from .import views

urlpatterns = [
    path('home_core', views.home_core, name="home_core"),

]
