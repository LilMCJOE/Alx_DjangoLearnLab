# Update Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book to be updated
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print("Updated book:", updated_book.title, updated_book.author, updated_book.publication_year)


# EXPECTED OUTPUT
#  Updated book: Nineteen Eighty-Four George Orwell 1949
