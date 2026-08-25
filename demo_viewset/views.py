from django.shortcuts import render

from rest_framework import viewsets

from demo_viewset.models import Book
from demo_viewset.serializers import BookSerializer

# Create your views here.

# CRUD automatique normal
# va faire tout tout seul :
# list, create, retrieve, update, partial_update, destroy

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

