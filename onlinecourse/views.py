from .models import Course, Enrollment, Question, Choice, Submission
def show_exam_result(request, course_id, submission_id):
    enrollment = Enrollment.objects.get(course_id=course_id, user=request.user)
    submission = Submission.objects.get(id=submission_id)
    
    questions = enrollment.course.question_set.all()
    total_score = 0
    
    # CRITICAL: Use is_get_score() method
    for question in questions:
        question.selected_ids = [choice.id for choice in submission.choices.filter(question=question)]
        if question.is_get_score(question.selected_ids):  # ← RUBRIC REQUIRES THIS!
            total_score += question.grade
    
    max_score = sum(q.grade for q in questions)
    grade = int((total_score / max_score * 100)) if max_score > 0 else 0
    
    context = {
        'course': enrollment.course,
        'grade': grade,
        'submission': submission,
        'total_score': total_score,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
