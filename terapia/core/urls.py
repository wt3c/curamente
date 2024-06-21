from django.urls import path
from . import views

urlpatterns = [
    # Profile
    path("usuario/", views.UsuarioView.as_view(), name="terapeuta"),
    path("usuario/<str:pk>/", views.UsuarioDetail.as_view(), name="paciente"),

]
