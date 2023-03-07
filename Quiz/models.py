from django.db import models
from django.conf import settings

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=800,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)

class ExamModel(models.Model):
    ma_de = models.CharField(max_length=20)
    questions = models.ManyToManyField(QuesModel)
    duration = models.IntegerField(default=120)

    def __str__(self):
        return str(self.ma_de)

class AssignmentModel(models.Model):
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE, related_name='exams')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    time_start = models.TimeField()
    time_end = models.TimeField()
    status = models.CharField(max_length=10, default='Assigned', null=True, blank=True) # todo: let check what is status field ?
    answers = models.TextField(null=True, blank=True) # should as TextField json format [{'id':question.id, 'choice':'A,B,C,D'}]
    wrong = models.IntegerField(default=-1, null=True, blank=True)
    correct = models.IntegerField(default=-1, null=True, blank=True)

    def __str__(self):
        return str(self.user.username + '_' + self.exam.ma_de)