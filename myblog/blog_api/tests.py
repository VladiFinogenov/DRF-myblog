from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post


class BlogPostTests(APITestCase):

    def setUp(self):
        """
        Настройка тестового пользователя.
        """

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_post(self):
        """
        Тест создания новой записи блога.
        """

        data = {'title': 'Test Post', 'content': 'Test Content', 'is_published': True}
        response = self.client.post('/api/v1/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_posts(self):
        """
        Тест получения списка записей блога.
        """

        response = self.client.get('/api/v1/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        """
        Тест обновления записи блога.
        """

        post = Post.objects.create(user=self.user, title='Test Post', content='Test Content', is_published=True)
        data = {'title': 'Updated Post', 'content': 'Updated Content', 'is_published': False}
        response = self.client.put(f'/api/v1/posts/{post.slug}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        """
        Тест удаления записи блога.
        """

        post = Post.objects.create(user=self.user, title='Test Post', content='Test Content', is_published=True)
        response = self.client.delete(f'/api/v1/posts/{post.slug}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)