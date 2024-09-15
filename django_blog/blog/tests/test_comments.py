from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment  # Correct import path

class CommentViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)

    def test_create_comment_requires_login(self):
        response = self.client.post(reverse('add_comment', kwargs={'post_id': self.post.id}), {'content': 'This is a comment'})
        self.assertRedirects(response, f'/login/?next=/post/{self.post.id}/comment/')

    def test_create_comment_success(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('add_comment', kwargs={'post_id': self.post.id}), {'content': 'This is a comment'})
        self.assertEqual(response.status_code, 302)  # Redirects after successful comment creation
        self.assertTrue(Comment.objects.filter(content='This is a comment').exists())

class CommentEditPermissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)
        self.comment = Comment.objects.create(content='Original Comment', author=self.user, post=self.post)

    def test_edit_comment_by_non_author(self):
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.post(reverse('edit_comment', kwargs={'comment_id': self.comment.id}), {'content': 'Edited Comment'})
        self.assertEqual(response.status_code, 403)  # Forbidden for non-author

    def test_edit_comment_by_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('edit_comment', kwargs={'comment_id': self.comment.id}), {'content': 'Edited Comment'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful edit
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Edited Comment')

class CommentDeletePermissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)
        self.comment = Comment.objects.create(content='Comment to delete', author=self.user, post=self.post)

    def test_delete_comment_by_non_author(self):
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.post(reverse('delete_comment', kwargs={'comment_id': self.comment.id}))
        self.assertEqual(response.status_code, 403)  # Forbidden for non-author

    def test_delete_comment_by_author(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_comment', kwargs={'comment_id': self.comment.id}))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
