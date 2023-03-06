from django.contrib import admin
from .models import TableClass, Student, TableChapter, TableLevel, TableAnswer
from .models import TableQuestion, TableExamStructure, TableExam, TableAssign, TableHelloThai
# Register your models here.
class TableClassAdmin(admin.ModelAdmin):
    list_display = ['name']

class TableStudentAdmin(admin.ModelAdmin):
    list_display = ['mssv', 'ho_va_chu_lot', 'ten', 'lop_hoc']

class AnswerInQuestion(admin.TabularInline):
    model = TableAnswer
    max_num = 4

class TableQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'chapter', 'level']
    list_filter = ['level']
    search_fields = ['question_text']
    inlines = [AnswerInQuestion]

admin.site.register(TableClass, TableClassAdmin)
admin.site.register(Student, TableStudentAdmin)
admin.site.register(TableChapter)
admin.site.register(TableLevel)
admin.site.register(TableAnswer)
admin.site.register(TableQuestion, TableQuestionAdmin)
admin.site.register(TableExamStructure)
admin.site.register(TableExam)
admin.site.register(TableAssign)
admin.site.register(TableHelloThai)