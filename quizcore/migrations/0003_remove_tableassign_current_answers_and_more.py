# Generated by Django 4.1.5 on 2023-03-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizcore', '0002_remove_student_lop_hoc_remove_student_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableassign',
            name='current_answers',
        ),
        migrations.AddField(
            model_name='tableassign',
            name='answers',
            field=models.TextField(blank=True, null=True),
        ),
    ]
