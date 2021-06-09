from django.shortcuts import render
from ssd_project_2021.models import Course


# Create your views here.
def home_page(request):
    courses = Course.objects.all()
    context = {'list_of_courses': courses}

    return render(request, 'home_page.html', context)


def course(request, course_id):
    found_course = Course.objects.get(pk=course_id)

    return render(request, 'course.html', {'course': found_course})
