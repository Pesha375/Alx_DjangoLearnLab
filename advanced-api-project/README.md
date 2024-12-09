# Advanced API Project

## Overview
This project demonstrates the use of Django REST Framework's generic views and mixins to handle CRUD operations for `Author` and `Book` models. It includes custom views for creating, retrieving, updating, and deleting authors and books, with appropriate permissions and custom behaviors.

## Models

### Author
- **Fields**:
  - `name` (CharField): The name of the author (max length: 100).

### Book
- **Fields**:
  - `title` (CharField): The title of the book (max length: 200).
  - `publication_year` (IntegerField): The year the book was published.
  - `author` (ForeignKey): The author of the book, linked to the `Author` model.
  - `owner` (User): The user who created the book.

## Views

### AuthorList (ListCreateAPIView)
- **Endpoint**: `/api/authors/`
- **Methods**: GET, POST
- **Permissions**: 
  - GET: Unauthenticated users can view all authors.
  - POST: Auth_required. Only authenticated users can create a new author.
- **Custom Behavior**: 
  - `perform_create`: Saves the author.

### AuthorDetail (RetrieveUpdateDestroyAPIView)
- **Endpoint**: `/api/authors/<int:pk>/`
- **Methods**: GET, PUT, DELETE
- **Permissions**: 
  - GET: Unauthenticated users can view a single author.
  - PUT, DELETE: Auth_required. Only authenticated users can update or delete an author.

### BookList (ListCreateAPIView)
- **Endpoint**: `/api/books/`
- **Methods**: GET, POST
- **Permissions**: 
  - GET: Unauthenticated users can view all books.
  - POST: Auth_required. Only authenticated users can create a new book.
- **Custom Behavior**: 
  - `perform_create`: Saves the book with the authenticated user as the owner.

### BookDetail (RetrieveUpdateDestroyAPIView)
- **Endpoint**: `/api/books/<int:pk>/`
- **Methods**: GET, PUT, DELETE
- **Permissions**: 
  - GET: Unauthenticated users can view a single book.
  - PUT, DELETE: Auth_required and ownership. Only the authenticated user who owns the book can update or delete it.
- **Custom Behavior**: 
  - `perform_update`: Saves the book with the authenticated user as the owner.

## Testing
- **Tools**: Postman, curl
- **Endpoints**:
  - Create a new author: POST `/api/authors/`
  - Retrieve all authors: GET `/api/authors/`
  - Retrieve a single author: GET `/api/authors/<int:pk>/`
  - Create a new book: POST `/api/books/`
  - Retrieve all books: GET `/api/books/`
  - Retrieve a single book: GET `/api/books/<int:pk>/`
  - Update a book: PUT `/api/books/<int:pk>/`
  - Delete a book: DELETE `/api/books/<int:pk>/`

## Permissions
- **IsOwnerOrReadOnly**: Custom permission class that allows read-only access to unauthenticated users and full access to authenticated users who own the book.
### Advanced Query Capabilities
#### Filtering
- Example: `/api/books/?author=Jane%20Austen`

#### Searching
- Example: `/api/books/?search=Pride`

#### Ordering
- Example: `/api/books/?ordering=publication_year