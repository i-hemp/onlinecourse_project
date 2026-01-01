from django.contrib import admin
from django.contrib.auth.models import User
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

# Inline classes
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# Custom admins
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course',)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'description')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Submission)
admin.site.register(Choice)
