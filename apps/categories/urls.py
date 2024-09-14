from django.urls import path 
from apps.categories.views import *

urlpatterns = [
    path('', CategoryAPIViews.as_view(), name='api_category'),
    path('', CategoryRetrieveAPIView.as_view(), name='api_category'),
    path('create', CategoryCreateAPIView.as_view(), name='api_category_create'),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='api_category_view'),
    path('delete/<int:pk>/', CategoryDestroyAPIView.as_view(), name='api_category_view'),
    
]