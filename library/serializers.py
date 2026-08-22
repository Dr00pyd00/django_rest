
from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """
    - normal : prend un objet AUTHOR et le transforme en dict python
            - serializers.data : le dict 
    - data= : prend du dict python et le transforme en obejt Author 
            - serializers.is_valid()
            - serializers.validated_data
            - serializers.save()
    """
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth']



class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'year']

