from django.db import models
from datetime import date


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_year = models.PositiveIntegerField()

    @property
    def book_age(self):
        return date.today().year - self.published_year

    def __str__(self):
        return f"{self.title} ({self.published_year})"
