"""
URL configuration for task_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('add_user',views.add_user, name = 'add_user'),
    path('add_task',views.add_task, name = 'add_task'),
    path('all_user_lists',views.all_user_lists, name = 'all_user_lists'),
    path('all_task_lists',views.all_task_lists, name = 'all_task_lists'),
    path('export/', views.export_users_tasks_xls, name='export_users_tasks_xls'),
]
