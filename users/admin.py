from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)

class StudentInCourse(admin.TabularInline):
    model = CourseStudentModel

@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'students']
    inlines = [StudentInCourse]

    def students(self, obj):
        return len(CourseStudentModel.objects.filter(course = obj))