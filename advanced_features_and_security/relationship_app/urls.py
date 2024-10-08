from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import register
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book
from . import views
urlpatterns = [
    path('add', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian', librarian_view, name='librarian_view'),
    path('member', member_view, name='member_view'),
    path('login', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register', views.register, name='register'),
    path('books', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
