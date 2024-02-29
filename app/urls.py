from django.urls import path , include
from app import views

urlpatterns = [
    path('',views.home, name='home'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    # path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]