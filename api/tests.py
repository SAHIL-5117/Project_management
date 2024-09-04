# api/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Client
from django.contrib.auth.models import User

class ClientTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_list_client_projects(self):
        response = self.client.get(f'/api/clients/{self.client_obj.id}/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_client(self):
        response = self.client.post('/api/clients/', {'client_name': 'Test Client', 'created_by': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_client(self):
        client = Client.objects.create(client_name='Test Client', created_by=self.user)
        response = self.client.get(f'/api/clients/{client.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client(self):
        client = Client.objects.create(client_name='Test Client', created_by=self.user)
        response = self.client.put(
            f'/api/clients/{client.id}/', 
            {'client_name': 'Updated Client'} 
        )
        print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_client(self):
        client = Client.objects.create(client_name='Test Client', created_by=self.user)
        response = self.client.delete(f'/api/clients/{client.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
