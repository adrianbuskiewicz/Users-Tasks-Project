from django.http import HttpResponse
from .models import User, Task
import requests
import csv


# Create your views here.

def update_db():
    """
    To be sure our app contains up to date data
    we need to clear the data previously had in our database.
    Then we download and save our data again in database.
    """

    User.objects.all().delete()
    Task.objects.all().delete()

    url = "https://jsonplaceholder.typicode.com/{}"

    users_data = requests.get(url=url.format('users'))
    users_json = users_data.json()

    tasks_data = requests.get(url=url.format('todos'))
    tasks_json = tasks_data.json()

    for user_data in users_json:
        user = User(**user_data)
        user.save()

    for task_data in tasks_json:
        user_id = task_data['userId']
        user = User.objects.get(id=user_id)
        task = Task(
            id=task_data['id'],
            title=task_data['title'],
            completed=task_data['completed'],
            user=user,
        )
        task.save()


def csv_file_view(request):
    update_db()
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment;'
                                        ' filename="users_tasks.csv"'},
    )

    tasks = Task.objects.all()
    writer = csv.writer(response)

    headers = [
            'name',
            'city',
            'title',
            'completed',
        ]

    writer.writerow(headers)

    for task in tasks:
        writer.writerow(
            [
                task.user.name,
                task.user.address['city'],
                task.title,
                task.completed,
            ]
        )
    return response

