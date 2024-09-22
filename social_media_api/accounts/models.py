from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    # following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        name='followers_set',
        through='Follow',
        through_fields=('follower', 'followed'),
    )
class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following_relations', on_delete=models.CASCADE)
    followed = models.ForeignKey(CustomUser, related_name='follower_relations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)