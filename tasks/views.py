from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.


def list_tasks(request):
    # connect to the database and fetch a queryset of tasks rows|instances
    tasks = Task.objects.all().order_by('-created_at')

    # create a context dictionary, i.e, things we want to show in the html interface/template
    context = {"tasks": tasks}

    # return response back
    return render(request, "tasks/list_tasks.html", context=context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        form.save()
        return redirect("task-list")
    else:
        context = {"form": TaskForm()}
        return render(request, "tasks/edit_task.html", context)


def edit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task-list")

    else:
        form = TaskForm(instance=task)

    context = {"form": form, "task": task}
    return render(request, "tasks/edit_task.html", context=context)


def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    task.delete()

    return redirect("task-list")


def toggle_complete(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    task.completed = False if task.completed else True

    task.save()

    return redirect("task-list")
