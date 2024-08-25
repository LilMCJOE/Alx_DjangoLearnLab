# Delete Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book to be deleted
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
remaining_books = Book.objects.all()
print("Remaining books:", remaining_books)


# Expected Output
# Remaining books: <QuerySet []>