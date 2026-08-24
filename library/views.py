
from django.shortcuts import get_object_or_404, render

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from library.models import Book, Author, Loan
from library.serializers import BookSerializer, AuthorSerializer, LoanSerializer 
# Create your views here.
# Va creer un FULL CRUD 
# obligation de donner un serializer  car va renvoyer du JSON  et pas du render html

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 



# ----------- LOANS ------------------------------------- #

# fonction simple 
@api_view(['POST'])
def create_loan_func(request):
    book = get_object_or_404(Book, pk=request.data['book'])
    if not book.is_available:
        return Response({'error':'book not available'}, status=status.HTTP_400_BAD_REQUEST)
    loan = Loan.objects.create(book=book, user=request.user)
    return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)

