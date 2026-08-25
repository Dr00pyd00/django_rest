
from rest_framework import serializers

from demo_viewset.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','year']


