from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView, BookListCreateView, BookDetailView

urlpatterns = [
    # Author APIs
    path("authors/", AuthorListCreateView.as_view(), name="author-list"),
     path("authors/create/", AuthorListCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),

    # Book APIs
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
