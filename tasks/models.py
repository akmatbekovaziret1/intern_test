from django.db import models


class Category(models.Model):
    category = models.CharField()
    
    
class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Tag(models.Model):
    tag = models.CharField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    