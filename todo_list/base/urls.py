from django.urls import path

from .views import TasksList

urlpatterns = [
    path('', TasksList.as_view(), name='tasks'),
]
