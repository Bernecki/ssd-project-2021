from django.contrib import admin

from ssd_project_2021.models import Course, Student, Teacher, School, Exam

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Exam)
