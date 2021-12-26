from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    address = models.JSONField()
    phone = models.CharField(max_length=300)
    website = models.CharField(max_length=300)
    company = models.JSONField()


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
