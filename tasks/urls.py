from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/edit/', views.project_update, name='project_update'),
    path('projects/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('projects/<int:project_id>/tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/edit/', views.task_update, name='task_update'),
]