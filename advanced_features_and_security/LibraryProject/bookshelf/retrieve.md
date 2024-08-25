# Retrieve Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book by title
retrieved_book = Book.objects.get(title="1984")
print("Retrieved book:", retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)


# EXPECTED OUTPUT
# Retrieved book: 1984 George Orwell 1949