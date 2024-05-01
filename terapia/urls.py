from django.contrib import admin
from django.urls import path, include
from .core import views as core_views, urls as core_urls

urlpatterns = [
    path("admin/", admin.site.urls),

    path ('', core_views.homepage, name='homepage'),
    path('login', core_views.login, name='login'),

    # Include core
    path("core/", include(core_urls)),

]
