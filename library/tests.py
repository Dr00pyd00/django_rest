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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)
        self.assertContains(response, self.book.title)

    def test_detail_book(self):
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['year'], self.book.year)
        self.assertContains(response, self.book.title)

    def test_create_book(self):
        payload1 =   {'author': self.author.id, 'title': 'La chute', 'year': 1956}
        payload2 =   {'author': self.author.id, 'title': 'A combat', 'year': 1947}
        res1 = self.client.post(reverse('book-list'), payload1)
        res2 = self.client.post(reverse('book-list'), payload2)

        self.assertEqual(res1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res1.data['title'], 'La chute')
        self.assertEqual(res2.data['title'], 'A combat')
        self.assertEqual(Book.objects.count(), 3)

    def test_delete_book(self):
        self.assertEqual(Book.objects.count(), 1)
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_update_book(self):
        new_data = {'title': 'TEST'}
        self.assertEqual(self.book.title, 'la peste')
        response = self.client.patch(reverse('book-detail', args=[self.book.id]), data=new_data, format='json') # type: ignore 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(response.data['title'], 'TEST')
        self.assertEqual(self.book.title, 'TEST')



