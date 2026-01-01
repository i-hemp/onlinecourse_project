from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.course.name}"

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # ← MISSING!
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=0)
    
    def is_get_score(self, selected_ids):  # ← MISSING!
        """Check if selected choice is correct"""
        correct_choice = self.choice_set.filter(is_correct=True).first()
        return correct_choice.id in selected_ids
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    
    def __str__(self):  # ← MISSING!
        return f"Submission {self.id} for {self.enrollment}"
