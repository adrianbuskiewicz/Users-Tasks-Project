from django.test import TestCase
from .models import User, Task
from .views import update_db
import csv
import io

# Create your tests here.


class TestApp(TestCase):

    def setUp(self):
        update_db()

    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 10)

    def test_tasks_count(self):
        tasks_count = Task.objects.all().count()
        self.assertEqual(tasks_count, 200)

    def test_specific_user(self):
        username = 'Samantha'
        email = "Nathan@yesenia.net"
        user_to_test = User.objects.get(id=3)
        self.assertEqual(user_to_test.username, username)
        self.assertEqual(user_to_test.email, email)

    def test_specific_task(self):
        update_db()
        title = "ipsa repellendus fugit nisi"
        completed = True
        task_to_test = Task.objects.get(id=12)
        self.assertEqual(task_to_test.title, title)
        self.assertEqual(task_to_test.completed, completed)

    def test_request(self):
        response = self.client.get("/app/user_task/")
        self.assertTrue(response.status_code==200)

    def test_downloaded_file(self):
        response = self.client.get("/app/user_task/")
        content = response.content.decode('utf-8')
        csv_reader = csv.reader((io.StringIO(content)))
        body = list(csv_reader)
        headers = body.pop(0)

        headers_row = ['name', 'city', 'title', 'completed']
        data_row_100th = ['Chelsey Dietrich', 'Roscoeview', 'excepturi a et neque qui expedita vel voluptate', 'False']

        self.assertEqual(headers_row, headers)
        self.assertEqual(data_row_100th, body[99])
