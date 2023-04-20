from django.urls import path

from . import views

from django.contrib.auth import views as viewPass

urlpatterns = [

    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutUser , name="logout"),
    path('register/', views.registerUser , name="register"),

    path('', views.profiles , name="profiles"),
    path('user_profile/<str:wk>', views.user_profile , name="user_profile"),
    path('account/', views.userAccount , name="account"),

    path('create_skill/', views.createSkill , name="create_skill"),
    path('edit_skill/<str:pk>', views.editSkill , name="edit_skill"),
    path('delete_skill/<str:pk>', views.deleteSkill , name="delete_skill"),

    path('edit_account/', views.editAccount , name="edit_account"),
    path('delete_Account/<str:wk>', views.deleteAccount , name="deleteAccount"),

    path('inbox', views.inbox , name="inbox"), 
    path('user_profile/<str:wk>/sendingMessage', views.sendingMessage , name="sendingMessage"),
    path('inbox/<str:pk>', views.message , name="message"),
    path('inbox/message/delete/<str:pk>', views.messageDelete , name="messageDelete"),

    path('edit_account/password_change' , viewPass.PasswordChangeView.as_view(template_name="password_change.html") , name='password_change'),
    path('edit_account/password_change/done' , viewPass.PasswordChangeDoneView.as_view(template_name="password_change_successful.html") ,
           name='password_change_done'),

              ]