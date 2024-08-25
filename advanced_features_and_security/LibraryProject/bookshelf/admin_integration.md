# Integrating the Book Model with Django Admin

## 1. Register the Book Model

**File:** `bookshelf/admin.py`

**Code:**
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
