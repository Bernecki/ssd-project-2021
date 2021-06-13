from django.shortcuts import render
from ssd_project_2021.models import *


def teacher_main(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    courses = Course.objects.filter(teacher=teacher_id)
    data = {'teacher': teacher, 'courses': {}}
    for course in courses:
        exams = Exam.objects.filter(course=course.id)
        data['courses'][course] = exams
    return render(request, 'teacher_main.html', data)
