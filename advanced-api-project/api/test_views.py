from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Set up a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create test data
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2001, owner=self.user)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2020, owner=self.user)
        self.book_create_data = {
            "title": "New Book",
            "author": "Author C",
            "publication_year": 2023
        }
        self.book_update_data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "publication_year": 2022
        }

    def test_list_books(self):
        # Test retrieving all books
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        # Test retrieving a single book
        response = self.client.get(f'/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        # Test creating a new book
        response = self.client.post('/books/', self.book_create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_create_data['title'])

    def test_update_book(self):
        # Test updating an existing book
        response = self.client.put(f'/books/{self.book1.id}/', self.book_update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_update_data['title'])

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(f'/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books(self):
        # Test filtering by author
        response = self.client.get('/books/?author=Author A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Author A")

    def test_search_books(self):
        # Test searching by title
        response = self.client.get('/books/?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books(self):
        # Test ordering by publication year
        response = self.client.get('/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2001)

    def test_permission_protection(self):
        # Test unauthenticated user access
        self.client.logout()
        response = self.client.post('/books/', self.book_create_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
