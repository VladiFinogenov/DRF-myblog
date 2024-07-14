from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import Post
from django.contrib.auth.models import User


class BlogPostTests(APITestCase):
    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create_user(username='user1', password='password1')
        self.client.force_authenticate(user=self.user)
        self.post_url = reverse('post-list-create')

    def test_create_update_delete_post(self):
        """
        Тест для проверки создания, изменения, и удаления поста.
        """

        # Создание поста
        data = {'title': 'Test Post', 'content': 'Test Content'}
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Обновление поста
        post_id = response.data['id']
        update_url = reverse('post_detail', kwargs={'pk': post_id})
        updated_data = {'title': 'Updated Post', 'content': 'Updated Content'}
        response = self.client.put(update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Удаление поста
        response = self.client.delete(update_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_modify_or_delete_post(self):
        """
        Тест проверяет, может ли другой пользователь изменять или удалять запись поста.
        """

        # Создание поста
        data = {'title': 'Test Post', 'content': 'Test Content'}
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Попытка другого пользователя изменить или удалить пост
        post_id = response.data['id']
        update_url = reverse('post_detail', kwargs={'pk': post_id})
        user2 = User.objects.create_user(username='user2', password='password2')
        self.client.force_authenticate(user=user2)

        # Попытка изменить пост
        updated_data = {'title': 'Updated Post', 'content': 'Updated Content'}
        response = self.client.put(update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Попытка удалить пост
        response = self.client.delete(update_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)