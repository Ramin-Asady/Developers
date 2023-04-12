from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutUser , name="logout"),
    path('register/', views.registerUser , name="register"),
    path('', views.profiles , name="profiles"),
    path('user_profile/<str:wk>', views.user_profile , name="user_profile"),
              ]