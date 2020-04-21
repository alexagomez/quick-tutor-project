from django.test import TestCase, RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from QuickTutor.models import Student, Tutor, TutorCourse, StudentRequest, Complaint
from QuickTutor.views import student, tutor, index, make_request, charge, tutorsession, studentsession, tutorpostsession, studentpostsession


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

#Written By: Brandie
#Test Case ID: T2_2.2, T2_1.2
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


#Written By: Brandie
#Test Case Id: T2_1.1
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
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

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        # Use this syntax for class-based views.
        self.assertEqual(response.status_code, 200)

#Written By: Alexa
#Test Case ID: T2_3.1
class TutorRequestTest(TestCase):
    def setUp(self):
        StudentRequest.objects.update_or_create(header ="django practice", description ="making the first web app", courseName="CS3240", location ="Clem", confusionMeter=2, studentEmail="abc1de@virginia.edu",)
        StudentRequest.objects.update_or_create(header ="normal distribution", description ="webwork problem set", courseName="APMA3100", location ="Clark", confusionMeter=7, studentEmail="fgh2ijk@virginia.edu",)
    
    def test_request_model(self):
        self.assertTrue(StudentRequest.objects.filter(header ="django practice").exists())
        self.assertTrue(StudentRequest.objects.filter(header ="normal distribution").exists())
        self.assertFalse(StudentRequest.objects.filter(header ="calc 3").exists())
        self.assertTrue(StudentRequest.objects.filter(description ="making the first web app",).exists())


#Written By: Soukarya
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class StudentPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')

    def test_details(self):
        request = self.factory.get('')
        request.user = self.user
        response = student(request)
        self.assertEqual(response.status_code, 200)

#Written By: Soukarya
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TutorPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')

    def test_details(self):
        request = self.factory.get('')
        request.user = self.user
        response = tutor(request)
        self.assertEqual(response.status_code, 200)

#Written By: Soukarya
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class MakeRequestPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')

    def test_details(self):
        request = self.factory.get('')
        request.user = self.user
        response = make_request(request)
        self.assertEqual(response.status_code, 200)

#Written By: Soukarya
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class ChargePageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')

    def test_details(self):
        try:
            request = self.factory.get('')
            request.user = self.user
            response = charge(request)

            # if it passes the request, it is function, so return true
            return True
        except:
            return False

#Written By: Alexa
class ComplaintTest(TestCase):
    def setUp(self):
        Complaint.objects.update_or_create(complainantUsername = 'chb8ue', complaineeUsername = 'abd9dd', description= 'silent the entire time')
        Complaint.objects.update_or_create(complainantUsername = 'jdj9er', complaineeUsername = 'kjh9hjj', description= 'showed up super late')
    
    def test_complaint_model(self):
        self.assertTrue(Complaint.objects.filter(complainantUsername = 'chb8ue').exists())
        self.assertFalse(Complaint.objects.filter(complainantUsername = 'oid0di').exists())
        self.assertTrue(Complaint.objects.filter(description = 'silent the entire time').exists())
        self.assertFalse(Complaint.objects.filter(description = 'never showed up').exists())
        self.assertTrue(Complaint.objects.filter(complaineeUsername = 'kjh9hjj').exists())

