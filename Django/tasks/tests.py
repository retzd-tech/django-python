# quotes/tests.py
from django.test import TestCase
from .models import Task
from django.test import Client

class TaskModelTest(TestCase):
    def test_str_output(self):
        task = Task.objects.create(title="Test Task", description="Test Description")
        self.assertEqual(task.title, "Test Task")

class TaskViewTest(TestCase):
    def test_get_tasks(self):
        client = Client()
        response = client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
