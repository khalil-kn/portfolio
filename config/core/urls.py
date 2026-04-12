from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('projects/', views.projects_list, name='projects_list'),
]