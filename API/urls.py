from django.urls import path

from . import views

urlpatterns = [
    path('',views.getRoutes),

    path('projects/',views.getProjects),
    path('projects/<str:pk>/',views.getProject),

    path('profiles/',views.getProfiles),
    path('profiles/<str:pk>/',views.getUserProfile),


]
