from rest_framework import status
from rest_framework.test import APITestCase


class UsersTEstCase(APITestCase):

    def test_create_user(self):
        """Тестирование создания пользователя"""
        data = {"email": "testuser2@mail.com", "password": "testuser2"}

        response = self.client.post("/users/register/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
