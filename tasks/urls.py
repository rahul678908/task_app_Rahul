from django.urls import path
from .views import TaskListCreate, TaskListView

urlpatterns = [
    path("view/", TaskListView.as_view(), name="task-list"),
    path("create/", TaskListCreate.as_view(), name="task-list-create"),
]
