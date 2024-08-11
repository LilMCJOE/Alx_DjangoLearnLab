# CRUD Operations for Book Model

## 1. Create a Book Instance

**Command:**
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Confirm creation
print("Book created:", book.title, book.author, book.publication_year)

