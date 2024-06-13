from django.urls import path
from . import views

urlpatterns = [
    # Profile
    path("terapeuta/", views.TerapeutaView.as_view(), name="terapeuta"),
    path("paciente/<str:pk>/", views.PacienteView.as_view(), name="paciente"),

]
