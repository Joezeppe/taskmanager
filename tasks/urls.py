from django.urls import path
from tasks import views

urlpatterns = [
    path("list/", views.list_tasks, name="task-list"),
    path("create/", views.create_task, name="task-create"),
    path("edit/<int:task_id>", views.edit_task, name="task-edit"),
    path("delete/<int:task_id>", views.delete_task, name="task-delete"),
    path(
        "toggle-complete/<int:task_id>",
        views.toggle_complete,
        name="task-toggle-complete",
    ),
]
