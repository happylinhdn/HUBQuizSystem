from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(QuesModel)
class QuesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']

@admin.register(ExamModel)
class ExamModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ma_de', 'duration']

@admin.register(AssignmentModel)
class AssignmentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'exam', 'user', 'status', 'answers', 'time_start', 'time_end']
