from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.projects , name="projects"),
    path('project/<str:pk>', views.single_project, name="single_project"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>',views.updateProject,name="update_project"),
]