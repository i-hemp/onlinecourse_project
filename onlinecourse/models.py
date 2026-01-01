from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self): return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self): return self.title

class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=False)

class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STUDENT = 'student'; DEVELOPER = 'developer'; DATA_SCIENTIST = 'data_scientist'
    OCCUPATION_CHOICES = [(STUDENT, 'Student'), (DEVELOPER, 'Developer'), (DATA_SCIENTIST, 'Data Scientist')]
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT)
    owner = models.BooleanField(default=False)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=0)
    
    def is_get_score(self, selected_ids):
        correct_choice = self.choice_set.filter(is_correct=True).first()
        return correct_choice.id in selected_ids if correct_choice else False
    
    def __str__(self): return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    def __str__(self): return f'Submission ID: {self.id}'
