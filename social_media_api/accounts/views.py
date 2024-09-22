from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import CustomUser
from posts.models import Post

# from .models import Post, Comment
# from .serializers import PostSerializer, CommentSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)




class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        # Use the serializer to validate the incoming data
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        # Get the authenticated user
        user = serializer.validated_data['user']
        
        # Get or create a token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        # Return the token and user ID in the response
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        }, status=status.HTTP_200_OK)
    # def post(self, request, *args, **kwargs):
    #     response = super().post(request, *args, **kwargs)
    #     token, created = Token.objects.get_or_create(user=response.data['user'])
    #     return Response({'token': token.key, 'user_id': response.data['user_id']})

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    def put(self, request):
        user = request.user
        if user.is_authenticated:
            # Perform profile update logic here
            return Response({"message": "Profile updated successfully"})
        else:
            return Response({"error": "User is not authenticated"}, status=401)
    def get_object(self):
        return self.request.user

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if request.user == user_to_follow:
        return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.add(user_to_follow)
    return Response({'detail': 'User followed successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({'detail': 'User unfollowed successfully'}, status=status.HTTP_200_OK)

def user_feed(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication required."}, status=401)

    # Get the users that the current user is following
    following_users = request.user.following.all()

    # Get the posts from the users that the current user follows
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    # Serialize the posts (you'll need to create a PostSerializer)
    post_data = PostSerializer(posts, many=True).data

    return Response(post_data, status=200)