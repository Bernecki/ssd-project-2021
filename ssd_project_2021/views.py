from django.shortcuts import render
from django.http import HttpResponse
from ssd_project_2021.models import Course
from ssd_project_2021.models import Student


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
    data = {'students' : students}
    return render(request,'student_page.html',data)

def choosen_student_achievements(request,id):
    students_achievements = Student.objects.get(pk=id)
    data = {'students' : students_achievements}
    return render(request,'student_achievements_page.html',data)

def choosen_student_previous_exam(request,id):
    students_exam = Student.objects.get(pk=id)
    data = {'students' : students_exam}
    return render(request,'student_previous_exam_page.html',data)

def choosen_student_taking_exam(request,id):
    students_taking_exam = Student.objects.get(pk=id)
    data = {'students' : students_taking_exam}
    return render(request,'student_taking_exam_page.html',data)

def choosen_student_courses(request,id):
    students_taking_exam = Student.objects.get(pk=id)
    data = {'students' : students_taking_exam}
    return render(request,'student_courses.html',data)