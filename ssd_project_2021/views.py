from django.shortcuts import render
from django.http import HttpResponse
from ssd_project_2021.models import *
from django.core import serializers
from .teacher import *
import datetime
from django.forms.models import model_to_dict
from django import forms
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def home_page(request):
    courses = Course.objects.all()
    context = {'list_of_courses': courses}

    return render(request, 'home_page.html', context)


def course(request, course_id):
    found_course = Course.objects.get(pk=course_id)

    return render(request, 'course.html', {'course': found_course})

def returningStudents(request):
    students = Student.objects.all()
    data = {'students' : students}
    return render(request,'students_page.html',data)

def choosen_student(request,id):
    students = Student.objects.get(pk=id)
    course1 = StudentCourse.object.all()
    data = {'students' : students, 'course' : course1}
    return render(request,'student_page.html',data)

def choosen_student_achievements(request,id):
    students_taking_courses = Student.objects.get(pk=id)
    student_course = StudentCourse.objects.values('student','course','final_grade')
    courses = Course.objects.all
    data = {'students' : students_taking_courses,
            'student_course': student_course,
            'courses':courses
            }
    return render(request,'student_achievements_page.html',data)

def choosen_student_previous_exam(request,id):
    students_exam = Student.objects.get(pk=id)
    assignment = Assignment.objects.values('student','exam','due_date','points','time_started','time_ended')
    date = datetime.datetime.now()
    data = {'students': students_exam,
            'assignment': assignment,
            'date':date}
    return render(request,'student_previous_exam_page.html',data)

def choosen_student_taking_exam(request,id,id2):
    students_taking_exam = Student.objects.get(pk=id)
    exam = Exam.objects.get(pk=id2)
    assignment = Assignment.objects.values('student', 'exam', 'due_date', 'points', 'time_started', 'time_ended')
    closed_question = ClosedQuestion.objects.all
    open_question = OpenQuestion.objects.all
    answer_to_closed_question = Answer.objects.all
    data = {'students': students_taking_exam,
            'assignment': assignment,
            'closed_question': closed_question,
            'open_question': open_question,
            'exam': exam,
            'answer_to_closed_question':answer_to_closed_question}
    return render(request,'student_taking_exam_page.html',data)

def choosen_student_choosing_exam_to_take(request,id):
    students_taking_exam = Student.objects.get(pk=id)
    assignment = Assignment.objects.values('student', 'exam', 'due_date', 'points', 'time_started', 'time_ended')
    closed_question = ClosedQuestion.objects.all()
    open_question = OpenQuestion.objects.all()
    exam = Exam.objects.all()
    data = {'students': students_taking_exam,
            'assignment': assignment,
            'closed_question': closed_question,
            'open_question': open_question,
            'exam': exam}
    return render(request,'student_choosing_exam_to_take.html',data)

def choosen_student_courses(request,id):
    students_taking_courses = Student.objects.get(pk=id)
    student_course = StudentCourse.objects.values('student','course','final_grade')
    data = {'students' : students_taking_courses, 'student_course': student_course}
    return render(request,'student_courses.html',data)

def choosen_student_data(request,id):
    students_taking_data = Student.objects.get(pk=id)
    school = School.objects.all
    data = {'students' : students_taking_data,
            'school': school}
    return render(request,'student_data.html',data)

def choosen_student_submitting_answers(request,id,id2):
    students_taking_exam = Student.objects.get(pk=id)
    exam = Exam.objects.get(pk=id2)
    assignment = Assignment.objects.values('student', 'exam', 'due_date', 'points', 'time_started', 'time_ended')
    closed_question = ClosedQuestion.objects.all
    open_question = OpenQuestion.objects.all
    answer_to_closed_question = Answer.objects.all
    answerClosed = request.POST.getlist('answerclosed')
    answerOpen = request.POST.getlist('answeropen')
    answerOpenQuestionId = request.POST.getlist('answeropenquestionid')
    points = []
    for a1 in answerClosed:
        points.append(Answer.objects.get(pk = a1))

    b=0
    for a in answerClosed:
        p=StudentAnswer(student_id = students_taking_exam.id, answer_id = a, is_selected = 1, points_for_answer = points[b].is_correct)
        p.save()
        b+=1

    b = 0
    for a in answerOpen:
        p = StudentOpenQuestion(student_id=students_taking_exam.id, open_question_id=answerOpenQuestionId[b], is_graded_by_teacher = 0,
                          points_for_answer=0,student_answer = a)
        p.save()
        b += 1


    data = {'students': students_taking_exam,
            'assignment': assignment,
            'closed_question': closed_question,
            'open_question': open_question,
            'exam': exam,
            'answer_to_closed_question': answer_to_closed_question,
            'answerclosed':answerClosed,
            'answeropen': answerOpen,
            'answerOpenQuestionId': answerOpenQuestionId
            }
    return render(request,'submitting_answers.html',data)

