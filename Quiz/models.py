# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from users.models import Profile, CourseModel

# Create your models here.
class QuesModel(models.Model):
    """Câu hỏi"""
    question = models.CharField(max_length=800, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    
    def __str__(self): 
        return self.question
        # if len(self.question) > 25:
        #     return self.question[0:25]
        # else:
        #     return self.question

class ExamModel(models.Model):
    """Đề thi"""
    ma_de = models.CharField(max_length = 50, default='Mã đề')
    duration = models.IntegerField(default = 120)

    def question_number(self):
        return len(ExamWithQuesRelated.objects.filter(exam = self))

    def __str__(self):
        return str(self.ma_de)

class ExamWithQuesRelated(models.Model):
    """Quan hệ Đề thi - Danh sách câu hỏi"""
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    question = models.ForeignKey(QuesModel, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('exam', 'question')

    def __str__(self):
        return self.exam.ma_de + ' - ' + self.question.question
    
class AssignmentSeason(models.Model):
    """Tên kỳ thi"""
    name = models.CharField(max_length=50) # Tên kỳ thi
    def __str__(self):
        return str(self.name)

class AssignmentRelated(models.Model):
    season = models.ForeignKey(AssignmentSeason, on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE, related_name='exams') #De Thi
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True) #Lớp, khóa học
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    
    status = models.CharField(max_length=10, default='Assigned', null=True, blank=True) # todo: let check what is status field ?
    answers = models.TextField(null=True, blank=True) # should as TextField json format [{'id':question.id, 'choice':'A,B,C,D'}]
    wrong = models.IntegerField(default=-1, null=True, blank=True)
    correct = models.IntegerField(default=-1, null=True, blank=True)
    class Meta:
        unique_together = ('season', 'student')


    def __str__(self):
        return self.season.name + ' - ' + self.exam.ma_de + ' - ' + (self.student and self.student.user.username or '')

class QuesSample(models.Model):
    """Câu hỏi ngân hàng đề"""
    question = models.CharField(max_length=800,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.question

class QuesMatrix(models.Model):
    """Ma trận câu hỏi"""
    name = models.CharField(max_length=200, default='Tên ma trận câu hỏi') #Ten ma tran -> Cau 1, de mau ABC
    def __str__(self):
        return str(self.name)

class QuesMatrixQuesSampleRelated(models.Model):
    """Ma trận câu hỏi - Ngân hàng đề"""
    matrix = models.ForeignKey(QuesMatrix, on_delete=models.CASCADE, related_name='matrix') #Ma trận
    question_sample = models.ForeignKey(QuesSample, on_delete=models.CASCADE, related_name='question_sample') #Câu hỏi mẫu
    class Meta:
        unique_together = ('matrix', 'question_sample')

    def __str__(self):
        return self.matrix.name + ' - ' + str(self.question_sample.question)

class QuizStructureSampleModel(models.Model):
    """Cấu trúc đề mẫu"""
    name = models.CharField(max_length=200, default='No Name')
    def __str__(self):
        return str(self.name)

class QuizStructureWithQuesMatrixRelated(models.Model):
    """Cấu trúc đề mẫu - Ma trận đề"""
    structure = models.ForeignKey(QuizStructureSampleModel, on_delete=models.CASCADE) #Tên cấu trúc
    matrix = models.ForeignKey(QuesMatrix, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('structure', 'matrix')

    def __str__(self):
        return str(self.structure.name) + ' - ' + str(len(QuizStructureWithQuesMatrixRelated.objects.filter(structure=self.structure))) + ' Câu hỏi'