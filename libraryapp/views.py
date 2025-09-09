from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm

# --- Book CRUD with CBV ---
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


# --- Author List + Create with FBV ---
@api_view(["GET", "POST"])
def author_list_create(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()

    # Handle Author form
    if request.method == "POST" and "author_submit" in request.POST:
        author_form = AuthorForm(request.POST, prefix="author")
        if author_form.is_valid():
            author_form.save()
            return redirect("/")
    else:
        author_form = AuthorForm(prefix="author")

    # Handle Book form
    if request.method == "POST" and "book_submit" in request.POST:
        book_form = BookForm(request.POST, prefix="book")
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm(prefix="book")

    context = {
        "authors": authors,
        "books": books,
        "author_form": author_form,
        "book_form": book_form,
    }
    return render(request, "home.html", context)
