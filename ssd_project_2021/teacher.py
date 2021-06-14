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
            open_question = OpenQuestion(text=question, exam=exam,time_limit = 1,character_limit = 400)
            open_question.save()

        for question in questions['closed']:
            closed_question = ClosedQuestion(text=question, exam=exam,time_limit = 1, more_than_one_answer = 1)
            closed_question.save()
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

def add_closed_question(request, teacher_id, course_id):
    global questions
    number_of_answers = request.GET.get('numberOfAnswers')
    if number_of_answers:
        number_of_answers = range(1, int(number_of_answers) + 1)

    previousAnswers = Answer.objects.all()
    previousQuestions = ClosedQuestion.objects.all()
    if request.method == 'POST':
        correct_answers = request.POST.getlist('correct_answers')
        question = request.POST.get('question')
        answers = request.POST.getlist('answer')
        questionId = request.POST.get('questionId')
        answerId = request.POST.get('answerId')
        helper = 1

        for a in answers:
            for c in correct_answers:
                print("ELO")
                print(helper)
                print(c)
                if helper==int(c):
                    p = Answer(id=int(answerId)+helper, text=a, is_correct = 1, closed_question_id=int(questionId)+1)
                    p.save()
                    break
                else:
                    p = Answer(id=int(answerId) + helper, text=a, is_correct=0, closed_question_id=int(questionId) + 1)
                    p.save()
            helper+=1


        questions['closed'].append(question)
        return redirect('/teacher/{}/add_exam/{}'.format(teacher_id, course_id))
    data = {'number_of_answers': number_of_answers,
            'previousAnswers': previousAnswers,
            'previousQuestions': previousQuestions}
    return render(request, 'add_closed_question.html',data)

def add_number_of_answers(request, teacher_id, course_id):
    global questions
    if request.method == 'POST':
        question = request.POST.get('question')
        questions['closed'].append(question)
        return redirect('/teacher/{}/add_exam/{}'.format(teacher_id, course_id))
    return render(request, 'answers_to_closed_question.html')


def add_assignment(request, teacher_id):
    student = Student.objects.all
    exam = Exam.objects.all
    data = {'student': student,
            'exam': exam}
    if request.method == 'POST':
        student_id1 =request.POST.get('student_id')
        exam_id1 = request.POST.get('exam_id')
        start_time1 = request.POST.get('start_time')
        end_time1 = request.POST.get('end_time')
        points1 = request.POST.get('points')
        p = Assignment(student_id = student_id1, exam_id=exam_id1, due_date=start_time1,points= points1 , time_started=start_time1,time_ended=end_time1 )
        p.save()

    return render(request, 'add_assignment.html', data)


