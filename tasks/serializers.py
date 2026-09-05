from rest_framework import serializers

from .models import Category, Task, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'category']


class TaskDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TagListSerializer(serializers.ModelSerializer):
    task = TaskListSerializer(read_only = True)

    class Meta:
        model = Tag
        fields = '__all__'


class TagDetailSerializer(serializers.ModelSerializer):
    task = TaskDetailSerializer(read_only = True)

    class Meta:
        model = Tag
        fields = '__all__'