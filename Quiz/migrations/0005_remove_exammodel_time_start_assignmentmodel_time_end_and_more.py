# Generated by Django 4.1.5 on 2023-03-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_exammodel_time_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exammodel',
            name='time_start',
        ),
        migrations.AddField(
            model_name='assignmentmodel',
            name='time_end',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='assignmentmodel',
            name='time_start',
            field=models.TimeField(auto_now=True),
        ),
    ]
