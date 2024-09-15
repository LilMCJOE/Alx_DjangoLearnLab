from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)

    def test_create_post_requires_login(self):
        response = self.client.get(reverse('post-create'))
        self.assertRedirects(response, '/login/?next=/post/new/')

    def test_edit_post_requires_login(self):
        response = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, f'/login/?next=/post/{self.post.pk}/edit/')

    def test_delete_post_requires_login(self):
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, f'/login/?next=/post/{self.post.pk}/delete/')

class PostAuthorPermissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)

    def test_post_edit_by_non_author(self):
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 403)

    def test_post_delete_by_non_author(self):
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 403)

    def test_post_edit_by_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)

    def test_post_delete_by_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
