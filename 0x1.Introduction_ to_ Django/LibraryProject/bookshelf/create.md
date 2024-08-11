# Create Operation

## Command
```python
from bookshelf.models import Book
Book.objects.create
# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Confirm creation
print("Book created:", book.title, book.author, book.publication_year)


# EXPECTED OUTPUT
# Book created: 1984 George Orwell 1949
