from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# -------------------
# Home page
# -------------------
def home(request):
    return render(request, "home.html")


# -------------------
# Author CBVs (CRUD)
# -------------------
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# -------------------
# Book CBVs (CRUD)
# -------------------
class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author_name = self.request.query_params.get("author")
        if author_name:
            queryset = queryset.filter(author__name__icontains=author_name)
        return queryset


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
