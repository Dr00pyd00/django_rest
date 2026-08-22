from django.shortcuts import render

from rest_framework import viewsets
from library.models import Book, Author
from library.serializers import BookSerializer, AuthorSerializer
# Create your views here.

# Va creer un FULL CRUD 
# obligation de donner un serializer  car va renvoyer du JSON  et pas du render html

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 



