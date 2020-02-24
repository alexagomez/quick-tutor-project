from django.test import TestCase
from QuickTutor.models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(email="abc1ef@virginia.edu", firstName="Alex")

    def test_student_template(self):
        self.assertEqual(3, 3)
        self.assertEqual(2, 2)