from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    