from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("libraryapp.urls")),   # Home and app URLs
    path("api/", include("libraryapp.urls")),  # API routes
]
