from django.urls import path 
from apps.post.views import *

urlpatterns = [
    path('', PostAPIView.as_view(), name='api_post'),
    path('create', PostAPICreate.as_view(), name='api_post_create'),
    path('update/<int:pk>/', PostUpdateAPIView.as_view(), name='api_post_view'),
    path('delete/<int:pk>/', PostDestroyAPIView.as_view(), name='api_destroy_view')
]