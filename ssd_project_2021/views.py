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