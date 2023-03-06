from django.contrib import admin
from .models import TableChapter, TableLevel, TableAnswer
from .models import TableQuestion, TableExamStructure, TableExam, TableAssign
# Register your models here.

class AnswerInQuestion(admin.TabularInline):
    model = TableAnswer
    max_num = 4

class TableQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'chapter', 'level']
    list_filter = ['level']
    search_fields = ['question_text']
    inlines = [AnswerInQuestion]

class TableExamAdmin(admin.ModelAdmin):
    list_display = ['ma_de', 'exam_structure', 'duration']
    list_filter = ['ma_de']
    search_fields = ['ma_de']
    #inlines = [QuestionInExam]

admin.site.register(TableChapter)
admin.site.register(TableLevel)
admin.site.register(TableQuestion, TableQuestionAdmin)
admin.site.register(TableExamStructure)
admin.site.register(TableExam, TableExamAdmin)
admin.site.register(TableAssign)