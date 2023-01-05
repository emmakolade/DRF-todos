from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase


class TestListCreateTodos(APITestCase):
    def test_creates_todos(self):
        self.client.post
