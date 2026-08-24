from django.shortcuts import get_object_or_404, render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from demo_function.models import Book
from demo_function.serializers import BookSerializer

# ici on va etre tres proche de fastapi : un decorateur puis une func 

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True) 
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def book_detail(request,pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['DELETE'])
def book_delete(request,pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def book_patch(request, pk):
    """
    Prend l'objet en DB, creer un serializer et met les data dedans avec partial si 
    jamais ya pas tout les champs,
    on verifie si c'est valid,
    on save
    """
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)








