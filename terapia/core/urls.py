from django.urls import path
from . import views

urlpatterns = [
    # Profile
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile-list/<str:pk>/", views.ProfileListView.as_view(), name="profile_list"),

]
