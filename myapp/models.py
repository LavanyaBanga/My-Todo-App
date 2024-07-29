from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.TextField()
    extra=models.CharField(max_length=255)
    created_at=models.DateField()
    is_completed=models.BooleanField(default=False)
    
