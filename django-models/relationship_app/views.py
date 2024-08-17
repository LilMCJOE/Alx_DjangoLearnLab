

# Create your views here.
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, '/Users/macbook/ALX_Projects/Alx_DjangoLearnLab/django-models/relationship_app/templates/relationship_app/library_detail.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'