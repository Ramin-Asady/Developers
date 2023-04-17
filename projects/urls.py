from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.projects , name="projects"),
    path('project/<str:pk>', views.single_project, name="single_project"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>',views.updateProject,name="update_project"),
    path('delete-project/<str:pk>',views.deleteProject,name="delete_project"),

    path('review/update/<str:pk>', views.reviewUpdate, name="reviewUpdate"),
    path('review/delete/<str:pk>', views.deleteReview, name="deleteReview"),
]