from django.db import models

# Create your models here.
class TableClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TableStudent(models.Model):
    mssv = models.CharField(max_length=20)
    ho_va_chu_lot = models.CharField(max_length=50)
    ten = models.CharField(max_length=20)
    lop_hoc = models.ForeignKey(TableClass, on_delete=models.CASCADE, related_name='lop_hoc')

class TableChapter(models.Model):
    chapter_name = models.CharField(max_length=50)
    def __str__(self):
        return self.chapter_name

class TableLevel(models.Model):
    level_name = models.CharField(max_length=50)
    def __str__(self):
        return self.level_name

class TableQuestion(models.Model):
    question_text = models.TextField()
    chapter = models.ForeignKey(TableChapter, on_delete=models.CASCADE, related_name='chapters')
    level = models.ForeignKey(TableLevel, on_delete=models.SET_NULL, related_name='levels', null=True)
    
    def __str__(self):
        return self.question_text

class TableAnswer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(TableQuestion, on_delete=models.CASCADE, related_name='question', null=True)
    def __str__(self):
        return self.text

class TableExamStructure(models.Model):
    year = models.IntegerField()
    chapters = models.ManyToManyField(TableChapter)
    def __str__(self):
        return self.year

class TableExam(models.Model):
    ma_de = models.CharField(max_length=20)
    questions = models.ManyToManyField(TableQuestion)
    exam_structure = models.ForeignKey(TableExamStructure, on_delete=models.CASCADE, related_name='exam_structure')
    duration = models.IntegerField()

class TableAssign(models.Model):
    exam = models.ForeignKey(TableExam, on_delete=models.CASCADE, related_name='exams')
    student = models.ForeignKey(TableStudent, on_delete=models.CASCADE, related_name='students')
    status = models.CharField(max_length=10) # todo: let check what is status field ?
    current_answers = models.ManyToManyField(TableAnswer)

class TableHelloThai(models.Model):
    note = models.CharField(max_length=20)
    def __str__(self):
        return self.note