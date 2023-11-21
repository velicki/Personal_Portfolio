from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/<str:pk>', views.projects, name='projects'),
    path('create-project/', views.projectForm, name='create-project'),
    path('update-project/<str:pk>', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>', views.deleteProject, name='delete-project'),
    path('update-about/<str:pk>', views.updateAbout, name='update-about'),
    path('add-topic/', views.newTopic, name='add-topic'),
    path('update-topic/<str:pk>', views.updateTopic, name='update-topic'),
    path('delete-topic/<str:pk>', views.deleteTopic, name='delete-topic'),
]