# Generated by Django 4.1.5 on 2023-01-20 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='apdate_at',
            new_name='update_at',
        ),
    ]
