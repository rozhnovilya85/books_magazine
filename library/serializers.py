from rest_framework import serializers
from .models import book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['pk', 'name', 'description', 'price', 'exist']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_firstname', 'author_name', 'author_patronymic', 'biography']

