from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _


# Create your models here.
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

MY_Chapter_example = (
        ('a', 'Chap 1'),
        ('b', 'Chap 2'),
        ('c', 'Chap 3'),
        ('d', 'Chap 4'),
    )

class TableExamStructure(models.Model):
    year = models.IntegerField()
    chapters = MultiSelectField(choices=MY_Chapter_example, max_length = 20, null=True)
    def __str__(self):
        return str(self.year)

class TableExam(models.Model):
    ma_de = models.CharField(max_length=20)
    questions = models.ManyToManyField(TableQuestion)
    exam_structure = models.ForeignKey(TableExamStructure, on_delete=models.CASCADE, related_name='exam_structure')
    duration = models.IntegerField()

    def __str__(self):
        return str(self.ma_de)

class TableAssign(models.Model):
    exam = models.ForeignKey(TableExam, on_delete=models.CASCADE, related_name='exams')
    #student = models.ForeignKey(TableStudent, on_delete=models.CASCADE, related_name='students')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10) # todo: let check what is status field ?
    answers = models.TextField(null=True, blank=True) # should as TextField json format [{'id':question.id, 'choice':'A,B,C,D'}]
    def __str__(self):
        return str(self.student.username + '_' + self.exam.ma_de)
