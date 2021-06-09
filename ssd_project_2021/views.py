from django.shortcuts import render
from ssd_project_2021.models import Course


# Create your views here.
def home_page(request):
    courses = Course.objects.all()
    context = {'list_of_courses': courses}

    return render(request, 'home_page.html', context)
