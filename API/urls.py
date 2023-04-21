from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 


urlpatterns = [
    path('',views.getRoutes),

    path('projects/',views.getProjects),
    path('projects/<str:pk>/',views.getProject),

    path('profiles/',views.getProfiles),
    path('profiles/<str:pk>/',views.getUserProfile),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
