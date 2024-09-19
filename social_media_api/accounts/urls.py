from django.urls import path
from .views import RegisterView, LoginView, ProfileView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('post/', PostViewSet),
    # path('comment/', CommentViewSet)
]

