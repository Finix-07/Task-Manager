from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user  # Set the created_by field to the current user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_form.html', {'form': form})

def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'tasks/project_form.html', {'form': form})

def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks/task_list.html', {'project': project, 'tasks': tasks})

def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project  # Set the project for the task
            task.created_by = request.user  # Set the created_by field to the current user
            task.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list', project_id=task.project.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'project': task.project})