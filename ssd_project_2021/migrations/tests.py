from django.test import TestCase
from ssd_project_2021.models import School
from ssd_project_2021.models import Teacher
import django
django.setup()

# Create your tests here.

class URL_Tests(TestCase):
    def test_testHomepageNot404(self):
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 404)


class AppModelsTests(TestCase):
    def test_model_str_School(self):
        name = School.objects.create(name="Test1")
        self.assertEqual(str(name), "Test1")

    def test_model_str_Teacher(self):
        name = Teacher.objects.create(name="Teacher_name_1")
        self.assertEqual(str(name), "Teacher_name_1")
