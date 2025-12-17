from django.contrib import admin
from django.urls import path, include

from accounts.views import profile_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", profile_view, name="home"),
]


