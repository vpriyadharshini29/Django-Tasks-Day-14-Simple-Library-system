from rest_framework import serializers
from datetime import date
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    book_age = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "published_year", "book_age"]

    def get_book_age(self, obj):
        return obj.book_age

    def validate_published_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Published year cannot be in the future.")
        return value
