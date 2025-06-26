from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")
        self.task_list_url = reverse("task-list")

    def authenticate(self):
        response = self.client.post(self.login_url, {"username": "testuser", "password": "testpass123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_user_registration(self):
        data = {"username": "newuser", "password": "newpass123"}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_login(self):
        response = self.client.post(self.login_url, {"username": "testuser", "password": "testpass123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_task_crud(self):
        self.authenticate()
        # Create
        data = {"title": "Test Task", "description": "desc", "completed": False}
        response = self.client.post(self.task_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task_id = response.data["id"]
        # List
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)
        # Retrieve
        url = reverse("task-detail", args=[task_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update
        response = self.client.patch(url, {"completed": True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["completed"])
        # Delete
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
