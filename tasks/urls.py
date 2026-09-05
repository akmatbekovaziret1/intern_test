from django.urls import path 
from . import views 

urlpatterns = [
    path('tasks/', views.TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailAPIView.as_view()),
    
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view()),
    
    path('tags/', views.TagListCreateAPIView.as_view()),
    path('tags/<int:pk>/', views.TagDetailAPIView.as_view()),
]

