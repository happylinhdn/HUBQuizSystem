from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class UserType(models.TextChoices):
    Teacher = 'Teacher', _('Teacher')
    Student = 'Student', _('Student')

class TableClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mssv = models.CharField(max_length=20, null=True)
    ho_va_chu_lot = models.CharField(max_length=50, null=True)
    ten = models.CharField(max_length=20, null=True)
    lop_hoc = models.ForeignKey(TableClass, on_delete=models.CASCADE, related_name='lop_hoc', null=True)

# @receiver(post_save, sender=User)
# def create_user_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_student(sender, instance, **kwargs):
#     instance.Student.save()

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

class TableAssign(models.Model):
    exam = models.ForeignKey(TableExam, on_delete=models.CASCADE, related_name='exams')
    #student = models.ForeignKey(TableStudent, on_delete=models.CASCADE, related_name='students')
    student2 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10) # todo: let check what is status field ?
    current_answers = models.ManyToManyField(TableAnswer)

class TableHelloThai(models.Model):
    note = models.CharField(max_length=20)
    def __str__(self):
        return self.note