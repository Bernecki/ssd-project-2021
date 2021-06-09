from django.db import models


# Create your models here.
class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    school_type = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=45)
    address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'school'


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    academic_degree = models.CharField(max_length=150, blank=True, null=True)
    email_address = models.CharField(max_length=200)
    school = models.ForeignKey(School, models.DO_NOTHING)
    login = models.CharField(unique=True, max_length=250)
    password = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'teacher'


# TODO Migrate to admin.py if needed
class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    login = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    email_address = models.CharField(max_length=200)
    school = models.ForeignKey('School', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin'


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    maxnumberofstudents = models.IntegerField(db_column='maxNumberOfStudents')  # Field name made lowercase.
    school = models.ForeignKey('School', models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'course'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    index_number = models.CharField(max_length=50)
    email_address = models.CharField(max_length=200)
    school = models.ForeignKey(School, models.DO_NOTHING)
    login = models.CharField(unique=True, max_length=250)
    password = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'student'


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    final_grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_course'


class Exam(models.Model):
    id = models.IntegerField(primary_key=True)
    duration = models.IntegerField()
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exam'


class Assignment(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    exam = models.ForeignKey('Exam', models.DO_NOTHING, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    time_started = models.DateTimeField(blank=True, null=True)
    time_ended = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'


class ClosedQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    more_than_one_answer = models.IntegerField()
    exam = models.ForeignKey('Exam', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'closed_question'


class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    is_correct = models.IntegerField()
    closed_question = models.ForeignKey('ClosedQuestion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    answer = models.ForeignKey(Answer, models.DO_NOTHING, blank=True, null=True)
    is_selected = models.IntegerField()
    points_for_answer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_answer'


class OpenQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    character_limit = models.IntegerField(blank=True, null=True)
    exam = models.ForeignKey(Exam, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_question'


class StudentOpenQuestion(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    open_question = models.ForeignKey(OpenQuestion, models.DO_NOTHING, blank=True, null=True)
    is_graded_by_teacher = models.IntegerField()
    points_for_answer = models.IntegerField(blank=True, null=True)
    student_answer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'student_open_question'
