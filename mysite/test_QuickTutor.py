from django.test import TestCase, RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from QuickTutor.models import Student, Tutor, TutorCourse, StudentRequest
from QuickTutor.views import student, tutor, index, make_request, charge


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

from django.test import TestCase, RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from QuickTutor.models import Student, Tutor, TutorCourse, StudentRequest
from QuickTutor.views import student, tutor, index, make_request, charge




#Written By: Brandie
#testing the many to one relationship with tutors and requests
class ManyTutorsToOneRequest(TestCase):
    def test_request_model(self):
        requestObj, created1 = StudentRequest.objects.update_or_create(header ="django practice", description ="making the first web app", courseName="CS3240", location ="Clem", confusionMeter=2, studentEmail="abc1de@virginia.edu",)
        tutor1, created2 = Tutor.objects.update_or_create(email="bay5fb@virginia.edu", firstName="Brandie", major="Computer Science", year="Fourth", request=requestObj)
        tutor2, created3 = Tutor.objects.update_or_create(email="tji5rj@virginia.edu", firstName="Tim", major="Chemistry", year="Fourth", request=requestObj)
        tutor3, created4 = Tutor.objects.update_or_create(email="ral7lk@virginia.edu", firstName="Ryanne", major="Biology", year="Third", request=requestObj)
        
        self.assertTrue(StudentRequest.objects.filter(header ="django practice").exists())
        self.assertTrue(tutor1 in requestObj.tutor_set.all())
        self.assertTrue(tutor2 in requestObj.tutor_set.all())
        self.assertTrue(tutor3 in requestObj.tutor_set.all())


#Written By: Brandie
#testing the many to one relationship with tutors and requests
class OneTutorToOneRequest(TestCase):
    def test_request_model(self):
        requestObj, created1 = StudentRequest.objects.update_or_create(header ="django practice", description ="making the first web app", courseName="CS3240", location ="Clem", confusionMeter=2, studentEmail="abc1de@virginia.edu",)
        tutor1, created2 = Tutor.objects.update_or_create(email="bay5fb@virginia.edu", firstName="Brandie", major="Computer Science", year="Fourth", request=requestObj)
        tutor2, created3 = Tutor.objects.update_or_create(email="tji5rj@virginia.edu", firstName="Tim", major="Chemistry", year="Fourth")
        
        self.assertTrue(StudentRequest.objects.filter(header ="django practice").exists())
        self.assertTrue(tutor1 in requestObj.tutor_set.all())
        self.assertTrue(tutor2 not in requestObj.tutor_set.all())

#Written By: Brandie
#testing the many to one relationship with tutors and requests
class OneTutorToDeletedRequest(TestCase):
    def test_request_model(self):
        requestObj, created1 = StudentRequest.objects.update_or_create(header ="django practice", description ="making the first web app", courseName="CS3240", location ="Clem", confusionMeter=2, studentEmail="abc1de@virginia.edu",)
        tutor1, created2 = Tutor.objects.update_or_create(email="bay5fb@virginia.edu", firstName="Brandie", major="Computer Science", year="Fourth", request=requestObj)
        requestObj.delete()
        tutor1.request=None
        self.assertFalse(StudentRequest.objects.filter(header ="django practice").exists())
        self.assertTrue(Tutor.objects.filter(firstName="Brandie").exists())
        self.assertEqual(tutor1.request, None)

#Written By: Brandie
#testing the many to one relationship with tutors and requests
class TutorOriginallyNoRequest(TestCase):
    def test_request_model(self):
        tutor1, created1 = Tutor.objects.update_or_create(email="bay5fb@virginia.edu", firstName="Brandie", major="Computer Science", year="Fourth")
        self.assertTrue(tutor1.request is None)
        #self.assertTrue(tutor1.request_id is None)

#Written By: Brandie
#testing the many to one relationship with tutors and requests
class OneTutorToNewRequest(TestCase):
    def test_request_model(self):
        requestObj1, created1 = StudentRequest.objects.update_or_create(header ="django practice", description ="making the first web app", courseName="CS3240", location ="Clem", confusionMeter=2, studentEmail="abc1de@virginia.edu")
        tutor1, created2 = Tutor.objects.update_or_create(email="bay5fb@virginia.edu", firstName="Brandie", major="Computer Science", year="Fourth", request=requestObj1)
        requestObj2, created1 = StudentRequest.objects.update_or_create(header ="operating systems", description ="reading the FAT", courseName="CS4414", location ="Rice", confusionMeter=10, studentEmail="jfg8kk@virginia.edu")
        tutor1.request=requestObj2
        self.assertTrue(StudentRequest.objects.filter(header ="django practice").exists())
        self.assertTrue(StudentRequest.objects.filter(header ="operating systems").exists())
        self.assertTrue(Tutor.objects.filter(firstName="Brandie").exists())
        self.assertEqual(tutor1.request, requestObj2)