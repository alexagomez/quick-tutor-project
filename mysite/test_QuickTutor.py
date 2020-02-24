from django.test import TestCase
<<<<<<< HEAD
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


=======
from QuickTutor.models import Student, Tutor, TutorCourse

#Brandie
class StudentModelTest(TestCase):
   # def setUp(self):
        
    def test_student_model(self):
        obj1, created1 = Student.objects.update_or_create(email="abc123@virginia.edu", firstName="Alex", lastName="Smith", major="Art", year="First")
        obj2, created2 = Student.objects.update_or_create(email="abc345@virginia.edu", firstName="Alex", lastName="Smith", major="Art", year="First")
        self.assertNotEquals(obj1.email, obj2.email)
        self.assertTrue(created1)
        self.assertTrue(created2)
        self.assertTrue(Student.objects.filter(email="abc123@virginia.edu").exists())
        self.assertTrue(Student.objects.filter(email="abc345@virginia.edu").exists())
        self.assertFalse(Student.objects.filter(email="hello@virginia.edu").exists())
        self.assertTrue(Student.objects.filter(firstName="Alex").exists())
>>>>>>> 47441e33e15f304a9047bddcf9914386236db84b
