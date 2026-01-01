# ADD to models.py:
class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=False)
    
class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
    ]
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT)
    owner = models.BooleanField(default=False)
