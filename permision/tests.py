from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class TestLaptopsViews(TestCase):

    def setUp(self):
        self.client.login(username='tester', password='test')

    def test_authentication_required(self):
        self.client.logout()
        url = reverse('Laptops_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
