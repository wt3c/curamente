from django.urls import path
from . import views

urlpatterns = [
    # Profile
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile-detail/<str:pk>/", views.ProfileViewDetail.as_view(), name="profile_detail"),

]
