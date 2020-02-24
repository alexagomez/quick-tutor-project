from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from QuickTutor.models import Student, Tutor, TutorCourse
from QuickTutor.views import student, tutor, index


# Written By: Soukarya
# Test Case ID: T2_1.1, T2_2.3
class TutorModelTest(TestCase):
    def setUp(self):
        Tutor.objects.update_or_create(email="tu10r@virginia.edu", firstName="TutorOne", major="Art", year="First")
        Tutor.objects.update_or_create(email="bob@virginia.edu", firstName="Bob", major="Computer Science", year="Third")

    def test_student_model(self):
        self.assertTrue(Tutor.objects.filter(email='tu10r@virginia.edu', firstName='TutorOne').exists())
        self.assertTrue(Tutor.objects.filter(email='bob@virginia.edu', firstName='Bob').exists())
        self.assertFalse(Tutor.objects.filter(email='dne@virginia.edu', firstName='NotReal').exists())

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


#Brandie
class LandingPageTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        # Use this syntax for class-based views.
        self.assertEqual(response.status_code, 200)

