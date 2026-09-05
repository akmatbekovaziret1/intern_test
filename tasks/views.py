from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Category, Task, Tag
from .serializers import (
    CategorySerializer,
    TaskListSerializer,
    TaskDetailSerializer,
    TaskCreateSerializer,
    TagListSerializer,
    TagDetailSerializer,
    TagCreateSerializer,
)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskListSerializer

        return TaskCreateSerializer


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TagListSerializer

        return TagCreateSerializer
    
class TagDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    
    