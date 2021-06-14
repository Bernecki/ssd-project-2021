from django.shortcuts import render, redirect
from ssd_project_2021.models import *

questions = {'open': [], 'closed': []}


def teacher_main(request, teacher_id):
    global questions
    questions = {'open': [], 'closed': []}

    teacher = Teacher.objects.get(pk=teacher_id)
    courses = Course.objects.filter(teacher=teacher_id)
    data = {'teacher': teacher, 'courses': {}}
    for course in courses:
        exams = Exam.objects.filter(course=course.id)
        data['courses'][course] = exams
    return render(request, 'teacher_main.html', data)


def teacher_add_exam(request, teacher_id, course_id):
    global questions
    if request.method == 'POST' and request.POST.get('submit_exam'):
        duration = int(request.POST.get('duration'))
        exam = Exam(duration=duration, teacher=Teacher.objects.get(pk=teacher_id),
                    course=Course.objects.get(pk=course_id))
        exam.save()
        for question in questions['open']:
            open_question = OpenQuestion(text=question, exam=exam)
            open_question.save()
        questions = {'open': [], 'closed': []}
        return redirect('/teacher/' + str(teacher_id))
    data = {'course_id': course_id,
            'questions': questions}
    return render(request, 'teacher_add_exam.html', data)


def add_open_question(request, teacher_id, course_id):
    global questions
    if request.method == 'POST':
        question = request.POST.get('question')
        questions['open'].append(question)
        return redirect('/teacher/{}/add_exam/{}'.format(teacher_id, course_id))
    return render(request, 'add_open_question.html')
