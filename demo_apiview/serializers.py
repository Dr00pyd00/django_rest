
from rest_framework import serializers

from demo_apiview.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','year']


