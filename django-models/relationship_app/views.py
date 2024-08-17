

# Create your views here.
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to the list_books view after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})