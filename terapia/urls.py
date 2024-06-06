from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .core import views as core_views, urls as core_urls




urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("login/", core_views.Login.as_view(), name="login"),
    path("core/", include(core_urls)),





]

urlpatterns = format_suffix_patterns(urlpatterns)