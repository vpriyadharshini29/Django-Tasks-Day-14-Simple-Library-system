from django import forms
from .models import Author, Book
from datetime import date

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year']

    def clean_published_year(self):
        year = self.cleaned_data.get('published_year')
        if year > date.today().year:
            raise forms.ValidationError("Published year cannot be in the future.")
        return year
