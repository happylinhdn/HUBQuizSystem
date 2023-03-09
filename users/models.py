# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class CourseModel(models.Model):
    """
    Khóa học
    """
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class CourseStudentModel(models.Model):
    """
    Khóa học vs Sinh Viên
    """
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='course_student_course')
    student_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='course_student_student_profle', null=True)

    class Meta:
        unique_together = ('course', 'student_profile')

    def __str__(self):
        return self.course.name + ' - ' + (self.student_profile and self.student_profile.user.username or 'No profile')