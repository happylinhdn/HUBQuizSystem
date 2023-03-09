from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(QuesModel)
class QuesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']

class QuesInExam(admin.TabularInline):
    model = ExamWithQuesRelated

@admin.register(ExamModel)
class ExamModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ma_de', 'duration']
    inlines = [QuesInExam]

class AssignmentInSesionQuestion(admin.TabularInline):
    model = AssignmentRelated
    #max_num = 4

@admin.register(AssignmentSeason)
class AssignmentSeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'assignment']
    inlines = [AssignmentInSesionQuestion]
    def assignment(self, season):
        relatedAssignments = AssignmentRelated.objects.filter(season = season)
        return relatedAssignments and len(relatedAssignments) or 0

@admin.register(QuesSample)
class QuesSampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']

class QuesSampleInQuesMatrix(admin.TabularInline):
    model = QuesMatrixQuesSampleRelated
    max_num = 4

@admin.register(QuesMatrix)
class QuesMatrixAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number_question']
    inlines = [QuesSampleInQuesMatrix]

    def number_question(self, obj):
        return len(QuesMatrixQuesSampleRelated.objects.filter(matrix=obj))

class MatrixInStructure(admin.TabularInline):
    model = QuizStructureWithQuesMatrixRelated

@admin.register(QuizStructureSampleModel)
class QuizStructureSampleModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [MatrixInStructure]

