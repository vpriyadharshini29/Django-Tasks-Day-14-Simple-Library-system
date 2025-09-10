from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # root welcome page
    path("api/", include("libraryapp.api_urls")),
]
