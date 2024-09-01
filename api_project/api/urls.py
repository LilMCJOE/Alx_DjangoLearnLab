from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('books/', BookList.as_view(), name='book-list'), 
]

router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
]