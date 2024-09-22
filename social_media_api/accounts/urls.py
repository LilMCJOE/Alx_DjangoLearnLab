from django.urls import path
from .views import user_feed, RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('post/', PostViewSet),
    # path('comment/', CommentViewSet)
    path('follow/<int:user_id>/', FollowUserView, name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView, name='unfollow_user'),
    path('feed/', user_feed, name='user_feed'),
]


