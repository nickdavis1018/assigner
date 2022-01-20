from django.db import models

# Create your models here.

class Assignment(models.Model):
    task = models.CharField(max_length=50)
    assignee = models.CharField(max_length=50)
    notes = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)