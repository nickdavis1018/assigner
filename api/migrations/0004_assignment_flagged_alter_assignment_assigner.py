# Generated by Django 4.0.1 on 2022-01-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_assignment_overdue'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='flagged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assigner',
            field=models.CharField(default='system', max_length=50),
        ),
    ]
