## Book API Views
- `BookListView`: Returns a list of all books (GET request to `/books/`).
- `BookDetailView`: Returns a single book by ID (GET request to `/books/<int:pk>/`).
- `BookCreateView`: Allows authenticated users to create a new book (POST request to `/books/create/`).
- `BookUpdateView`: Allows authenticated users to update a book (PUT or PATCH request to `/books/<int:pk>/update/`).
- `BookDeleteView`: Allows authenticated users to delete a book (DELETE request to `/books/<int:pk>/delete/`).
