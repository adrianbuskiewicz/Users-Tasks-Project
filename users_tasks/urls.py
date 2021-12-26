from django.urls import path
from .views import csv_file_view

urlpatterns = [
    path('user_task/', csv_file_view)
]
