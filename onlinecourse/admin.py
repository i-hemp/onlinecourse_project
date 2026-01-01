from django.contrib import admin
from .models import Question, Choice, Submission
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question
    inlines = [ChoiceInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(User, UserAdmin)
admin.site.register(ContentType)
admin.site.register(Session)
