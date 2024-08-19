from . import views
from django.urls import path

urlpatterns = [
    path('',views.loginView,name='main'),
    path('home/<str:pk>/',views.homeView,name = 'home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginView,name='login'),
    path('delteTask/<int:taskID>/',views.deleteTask,name='deleteTask'),
    path('updateTask/<int:taskID>/',views.updateTask,name="updateTask"),
    path('logout/',views.logoutUser,name='logout'),
]