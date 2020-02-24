from django.test import TestCase
from QuickTutor.models import Student, Tutor

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(email="abc1ef@virginia.edu", firstName="Alex")

    def test_student_template(self):
        self.assertEqual(3, 3)
        self.assertEqual(2, 2)


# Written By: Soukarya
# Test Case ID: T2_1.1, T2_2.3
class TutorModelTest(TestCase):
    def setUp(self):
        Tutor.objects.create(email="tu10r@virginia.edu", firstName="TutorOne")
        Tutor.objects.create(email="bob@virginia.edu", firstName="Bob")

    def test_student_model(self):
        self.assertTrue(Tutor.objects.filter(email='tu10r@virginia.edu', firstName='TutorOne').exists())
        self.assertTrue(Tutor.objects.filter(email='bob@virginia.edu', firstName='Bob').exists())
        self.assertFalse(Tutor.objects.filter(email='dne@virginia.edu', firstName='NotReal').exists())


