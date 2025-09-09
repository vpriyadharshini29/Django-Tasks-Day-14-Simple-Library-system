from django.urls import path
from .views import BookListCreateView, BookDetailView, author_list_create, home

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", author_list_create, name="author-list-create"),
]
