from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status 
from library.models import Book, Author


# Create your tests here.

# ======================================================== #
# Response: 
# .headers : metadonnees 
# .data : exemple liste d'object , contenu du json ?

class BookAPITests(APITestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(name='Albert Camus', birth='1913-07-11')
        self.book = Book.objects.create(author=self.author, title='la peste', year=1968)

    def test_list_book(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)
        self.assertContains(response, self.book.title)

    def test_detail_book(self):
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['year'], self.book.year)
        self.assertContains(response, self.book.title)
        print(response.data['id'])


