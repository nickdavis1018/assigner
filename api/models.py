from django.db import models

# Create your models here.

class Assignment(models.Model):
    task = models.CharField(max_length=50)
    assignee = models.CharField(max_length=50)
    assigner = models.CharField(max_length=50, default="system")
    notes = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    overdue = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    urgency = models.BooleanField(default=False)