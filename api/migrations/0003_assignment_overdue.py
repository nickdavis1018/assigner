# Generated by Django 4.0.1 on 2022-01-25 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_assignment_assigner_assignment_urgency'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='overdue',
            field=models.BooleanField(default=False),
        ),
    ]