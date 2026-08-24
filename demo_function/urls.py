
from django.urls import path

from demo_function.views import book_list, book_create, book_detail, book_delete, book_patch

urlpatterns = [
        path('books/', book_list, name='demo-function-book-list'),
        path('books/create/', book_create, name='demo-function-book-create'),
        path('books/<int:pk>/', book_detail, name='demo-function-book-detail'),
        path('books/delete/<int:pk>/', book_delete, name='demo-function-book-delete'),
        path('books/patch/<int:pk>/', book_patch, name='demo-function-book-patch'),
        ]
