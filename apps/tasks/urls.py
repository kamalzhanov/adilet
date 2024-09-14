from django.urls import path 
from apps.tasks.views import *

urlpatterns = [
    path('', TaskAPIView.as_view(), name='api_task'),
    path('create', TaskAPICreate.as_view(), name='api_task_create'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='api_task_view'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='api_destroy_view')
]