from django.db import models
from django.contrib.auth.models import User

# ADD THESE BASE MODELS:
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Enrollment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

class Course(models.Model):
    name = models.CharField(max_length=200)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

# YOUR EXISTING MODELS (KEEP):
class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=200)
    grade = models.IntegerField(default=0)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    choices = models.ManyToManyField(Choice)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    grade = models.FloatField(default=0.0)
