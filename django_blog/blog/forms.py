# blog/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import Comment
from taggit.forms import TagWidget

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','tags']
        widgets = {
            'tags': TagWidget(attrs={'class': 'tag-input', 'placeholder': 'Add tags here'}),
    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']