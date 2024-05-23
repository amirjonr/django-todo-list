from django.urls import path

from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task'),
]
