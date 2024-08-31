from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
]