from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from django.utils.decorators import decorator_from_middleware



@login_required
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic for editing the book goes here
    return render(request, 'edit_book.html', {'book': book})

@login_required
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})

def csp_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trusted.cdn.com"
        return response
    return middleware

@decorator_from_middleware(csp_middleware)
def secure_view(request):
    pass

def secure_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    