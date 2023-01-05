from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from todos.models import Todo


class TodosAPITestCase(APITestCase):
    def create_todo(self):
        sample_todo = {'title': 'hello', 'description': 'test'}
        response = self.client.post(reverse('todos'), sample_todo)

    def authenticate(self):
        self.client.post(reverse("register"), {
                         'username': 'username', 'email': 'email@gmail.com', 'password': 'password123'})
        response = self.client.post(reverse('login'), {
            'email': 'email@gmail.com', 'password': 'password123'})
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")


class TestListCreateTodos(TodosAPITestCase):

    def test_should_not_create_todos_with_no_auth(self):
        respoonse = self.create_todo()
        self.assertEqual(respoonse.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate()
        respoonse = self.create_todo()
        self.assertEqual(Todo.objects.all().count(), previous_todo_count + 1)
        self.assertEqual(respoonse.status_code, status.HTTP_201_CREATED)
        self.assertEqual(respoonse.data['title'], 'Hello')
        self.assertEqual(respoonse.data['description'], 'test')

    def test_retrieves_all_todos(self):
        self.authenticate()
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)
        self.create_todo()
        res = self.client.get(reverse('todos'))
        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)


class TestTodoDetailApiView(TodosAPITestCase):
    def test_retrieves_one_item(self):
        self.authenticate()
        response = self.create_todo()
        res = self.client.get(
            reverse('todo', kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        todo = Todo.objects.get(id=response.data['id'])
        self.assertEqual(todo.title, res.data['title'])

    def test_updates_one_item(self):
        self.authenticate()
        response = self.create_todo()
        res = self.client.patch(reverse('todo', kwargs={'id': response.dada['id']}), {
                                'title': 'new', 'is_complete': True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        updated_todo = Todo.objects.get(id=response.data['id'])
        self.asserEqual(updated_todo.is_complete, True)
        self.asserEqual(updated_todo.title, 'New')

    def test_deletes_one_item(self):
        self.authenticate()
        res = self.create_todo()
        previous_db_count = Todo.objects.all().count()
        self.assertGreater(previous_db_count, 0)
        self.assertEqual(previous_db_count, 1)
        response = self.client.delete(
            reverse('todo', kwargs={'id': res.dada['id']}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.all().count(), 0)
