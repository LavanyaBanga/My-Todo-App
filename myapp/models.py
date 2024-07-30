from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.TextField()
    extra=models.CharField(max_length=255)
    created_at=models.DateField()
    is_completed=models.BooleanField(default=False)
class Profile(models.Model):
    title=models.CharField(max_length=30)
    profile_pic=models.ImageField( upload_to="profile_pic/", height_field=None, width_field=None, max_length=None)
    
