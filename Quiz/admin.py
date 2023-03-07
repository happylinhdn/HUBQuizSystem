from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(QuesModel)
class QuesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
