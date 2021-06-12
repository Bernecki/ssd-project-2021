"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ssd_project_2021.views import *


urlpatterns = [
    path('examsystem/', include('ssd_project_2021.urls')),
    path('admin/', admin.site.urls),
    path('student/', returningStudents),
    path('student/<id>/', choosen_student),
    path('student/<id>/achievements', choosen_student_achievements),
    path('student/<id>/previous_exam', choosen_student_previous_exam),
    path('student/<id>/taking_exam', choosen_student_taking_exam),
    path('student/<id>/courses', choosen_student_courses),
]
