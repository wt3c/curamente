from django.urls import path
from . import views

urlpatterns = [
    #
    # Profile
    path("profile/", views.ProfileView.as_view(), name="profile"),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
