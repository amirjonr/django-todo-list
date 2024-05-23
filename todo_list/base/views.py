from django.views.generic.list import ListView

from .models import Task


# Create your views here.

class TasksList(ListView):
    model = Task
