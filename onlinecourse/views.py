from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Enrollment, Question, Choice, Submission

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user_enrollment = Enrollment.objects.filter(user=request.user, course=course)
    context = {'course': course}
    if request.user.is_authenticated:
        context['enrollment'] = user_enrollment.first()
    return render(request, 'onlinecourse/course_details_bootstrap.html', context)

def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    enrollment = Enrollment.objects.get_or_create(user=user, course=course)[0]
    enrollment.save()
    return HttpResponseRedirect(reverse('onlinecourse:course_details', args=[course.id]))

def submit(request, course_id):
    enrollment = Enrollment.objects.get(course_id=course_id, user=request.user)
    questions = enrollment.course.question_set.all()
    
    submission = Submission.objects.create(enrollment=enrollment)
    for question in questions:
        choice_id = int(request.POST.get(f'choice_{question.id}', 0))
        if choice_id:
            choice = Choice.objects.get(id=choice_id)
            submission.choices.add(choice)
    
    submission.save()
    return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=[course_id, submission.id]))

def show_exam_result(request, course_id, submission_id):
    enrollment = Enrollment.objects.get(course_id=course_id, user=request.user)
    submission = Submission.objects.get(id=submission_id)
    
    questions = enrollment.course.question_set.all()
    total_score = 0
    grade = 0
    
    for question in questions:
        correct_choice = question.choice_set.filter(is_correct=True).first()
        user_choice = submission.choices.filter(question=question).first()
        if correct_choice and user_choice == correct_choice:
            total_score += question.grade
    
    if questions.count() > 0:
        grade = int((total_score / sum(q.grade for q in questions)) * 100)
    
    context = {
        'course': enrollment.course,
        'grade': grade,
        'submission': submission,
        'total_score': total_score,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
