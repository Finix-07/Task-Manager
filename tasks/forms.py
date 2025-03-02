from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']  # Fields to include in the form

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority', 'project', 'assigned_to']