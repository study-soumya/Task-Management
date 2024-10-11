from django.urls import path
from .views import TaskListCreateView, TaskDetailView, NotificationListView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('notifications/', NotificationListView.as_view(),
         name='notification-list'),
]
