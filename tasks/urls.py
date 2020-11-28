from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskApp, name='taskApp'),
    path('del_task/<str:pk>/', views.del_task, name='del_task'),
    path('update_task/<str:pk>/', views.update_task, name='update_task')
]