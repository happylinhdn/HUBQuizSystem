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
    list_display = ['id', 'assignment_season', 'exam', 'user', 'status', 'answers', 'time_start', 'time_end']

class AssignmentInSesionQuestion(admin.TabularInline):
    model = AssignmentModel
    #max_num = 4

@admin.register(AssignmentSeason)
class AssignmentSeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'assignment']
    inlines = [AssignmentInSesionQuestion]
    def assignment(self, season):
        relatedAssignments = AssignmentModel.objects.filter(assignment_season = season)
        return relatedAssignments and len(relatedAssignments) or 0

@admin.register(QuizMatrix)
class QuizMatrixAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_of_matrix']

@admin.register(QuizSample)
class QuizSampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_of_sample']

@admin.register(QuesSample)
class QuesSampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
