
from django.contrib import admin
from django.urls import path
from TodoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("start/",views.Start,name="start"),
    path("start/createtask/",views.CreateTask,name="createtask"),
    path("complete/<int:id>/",views.CompleteTask,name="completetask"),
    path("deletetask/<int:id>",views.DeleteTask,name="deletetask"),
    path("history/",views.History,name="history"),
    path("progress/",views.progress,name="progress"),                                       
                
]
