from django.test import TestCase, RequestFactory, override_settings
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser, User
from QuickTutor.models import Student, Tutor, TutorCourse, StudentRequest, Complaint
from QuickTutor.views import student, tutor, index, make_request, charge, tutorsession, studentsession, tutorpostsession, studentpostsession, checkstart, checkaccepted, checkrequestcount, checkacceptedtutorcount, checksessionstudent
from django.test import TestCase, RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from QuickTutor.models import Student, Tutor, TutorCourse, StudentRequest, Message
from QuickTutor.views import student, tutor, index, make_request, charge, store_message, get_message, edit_student, edit_tutor
import json

# Written By: Soukarya
# Test Case ID: T1.1, T1.2
class TutorModelTest(TestCase):
    def setUp(self):
        Tutor.objects.update_or_create(email="tu10r@virginia.edu", firstName="TutorOne", major="Art", year="First")
        Tutor.objects.update_or_create(email="bob@virginia.edu", firstName="Bob", major="Computer Science", year="Third")

    def test_student_model(self):
        self.assertTrue(Tutor.objects.filter(email='tu10r@virginia.edu', firstName='TutorOne').exists())
        self.assertTrue(Tutor.objects.filter(email='bob@virginia.edu', firstName='Bob').exists())
        self.assertFalse(Tutor.objects.filter(email='dne@virginia.edu', firstName='NotReal').exists())

#Written By: Brandie
#Test Case ID: T2.1, T2.2
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
#Test Case ID: T3.1, T3.2
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
        request.user = self.user

        response = index(request)
        self.assertEqual(response.status_code, 200)

#Written By: Alexa
#Test Case ID: T4.1, T4.2
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
#Test Case ID: T5.1, T5.2
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
#Test Case ID: T6.1, T6.2
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
#Test Case ID: T7.1, T7.2
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
#Test Case ID: T8.1, T8.2
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
#Test Case ID: T9.1, T9.2
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

#Written By: Brandie
#testing the many to one relationship with tutors and requests
#Test Case ID: T10.1
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
#Test Case ID: T11.1
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
#Test Case ID: T12.1
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
#Test Case ID: T13.1
class TutorOriginallyNoRequest(TestCase):
    def test_request_model(self):
        tutor1, created1 = Tutor.objects.update_or_create(email="bay5fb@virginia.edu", firstName="Brandie", major="Computer Science", year="Fourth")
        self.assertTrue(tutor1.request is None)
        #self.assertTrue(tutor1.request_id is None)

#Written By: Brandie
#testing the many to one relationship with tutors and requests
#Test Case ID: T14.1
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

#Written By: Greg
#Test Case ID: T15.1, T15.2
class CheckStart(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)

        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="tutor@virginia.edu",
            tutorUsername="tutor",
            sessionEnded=0,
            deleteStatus=0
        )

    def test_checkstart(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        jsonResponse = json.loads(checkstart(request).content)[0]
        self.assertEqual(jsonResponse["status"], 0)

#Written By: Greg
#Test Case ID: T16.1, T16.2
class CheckAccepted(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="user@virginia.edu",
            tutorUsername="user",
            sessionEnded=0,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="user@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_checkaccepted(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        jsonResponse = json.loads(checkaccepted(request).content)[0]
        self.assertEqual(jsonResponse['accepted'], 1)

#Written By: Greg
#Test Case ID: T17.1, T17.2
class CheckRequestCount(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="user@virginia.edu",
            tutorUsername="user",
            sessionEnded=0,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="user@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_checkrequestcount(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        jsonResponse = json.loads(checkrequestcount(request).content)[0]
        self.assertEqual(jsonResponse['requestCount'], 0)

#Written By: Greg
#Test Case ID: T18.1, T18.2
class CheckAcceptedTutorCount(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="user@virginia.edu",
            tutorUsername="user",
            sessionEnded=0,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="user@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_checkacceptedtutorcount(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        jsonResponse = json.loads(checkacceptedtutorcount(request).content)[0]
        self.assertEqual(jsonResponse['acceptedTutorCount'], 1)

#Written By: Greg
#Test Case ID: T19.1, T19.2
class CheckSessionStudent(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='user@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="user@virginia.edu",
            tutorUsername="user",
            sessionEnded=1,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="user@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_checksessionstudent(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        jsonResponse = json.loads(checksessionstudent(request).content)[0]
        self.assertEqual(jsonResponse['sessionEnded'], 1)

#Written By: Alexa
#Test Case ID: T21.1, T21.2
class StudentPostSessionPage(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='student@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="tutor@virginia.edu",
            tutorUsername="tutorUser",
            sessionEnded=1,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="tutor@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_studentpostsession(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        studentRequestHeader = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').header
        tutorUsername = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').tutorUsername
        response = studentpostsession(request, studentRequestHeader = studentRequestHeader, tutorUsername= tutorUsername)
        
        self.assertEqual(response.status_code, 200)


#Written By: Alexa
#Test Case ID: T22.1, T22.2
class TutorPostSessionPage(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='student@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="tutor@virginia.edu",
            tutorUsername="tutorUser",
            sessionEnded=1,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="tutor@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_tutorpostsession(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        studentRequestHeader = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').header
        studentUsername = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').studentUsername
        response = tutorpostsession(request, studentRequestHeader = studentRequestHeader, studentUsername= studentUsername)
        
        self.assertEqual(response.status_code, 200)

#Written By: Alexa
#Test Case ID: T23.1, T23.2
class StudentPostSession(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='student@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="tutor@virginia.edu",
            tutorUsername="tutorUser",
            sessionEnded=1,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="tutor@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_studentpostsession(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        studentRequestHeader = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').header
        tutorUsername = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').tutorUsername
        response = studentpostsession(request, studentRequestHeader = studentRequestHeader, tutorUsername= tutorUsername)
        
        self.assertEqual(StudentRequest.objects.get(studentEmail = 'student@virginia.edu').sessionEnded, 1)


#Written By: Alexa
#Test Case ID: T24.1, T24.2
class TutorPostSession(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='student@virginia.edu', password='top_secret')
        self.student = Student.objects.update_or_create(email=self.user.email, username=self.user.username)
        
        courseName = "Course Name"
        header = "Course Header"
        description = "This is a course description"
        location = "The location"
        status = 0
        meetingDetails = "Meeting details"
        confusionMeter = 5
        studentEmail = self.user.email
        studentUsername = self.user.username

        

        req, obj = StudentRequest.objects.update_or_create(
            courseName=courseName, 
            header=header, 
            description=description, 
            location=location, 
            status=status,
            meetingDetails=meetingDetails, 
            confusionMeter=confusionMeter, 
            studentEmail=studentEmail, 
            studentUsername=studentUsername,
            tutorEmail="tutor@virginia.edu",
            tutorUsername="tutorUser",
            sessionEnded=1,
            deleteStatus=0
        )

        self.tutor, obj = Tutor.objects.update_or_create(
                    email="tutor@virginia.edu"
        )
        self.tutor.request = req
        self.tutor.save(update_fields=['request'])

    def test_tutorpostsession(self):
        request = self.factory.get('')
        request.user = self.user
        request.student = self.student
        studentRequestHeader = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').header
        studentUsername = StudentRequest.objects.get(studentEmail = 'student@virginia.edu').studentUsername
        response = tutorpostsession(request, studentRequestHeader = studentRequestHeader, studentUsername= studentUsername)
        
        self.assertEqual(StudentRequest.objects.get(studentEmail = 'student@virginia.edu').sessionEnded, 1)
        self.assertEqual(Tutor.objects.get(email = 'tutor@virginia.edu').status, 0)
        self.assertEqual(Student.objects.get(email = 'student@virginia.edu').status, 0)
        self.assertEqual(Student.objects.get(email = 'student@virginia.edu').accepted, 0)
        

# ---------- MESSAGES -----------
# Written By: Soukarya
class StoreMessageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tutor', email='tutor@virginia.edu', password='top_secret')
        Tutor.objects.update_or_create(email="tutor@virginia.edu", firstName="Bob", major="Computer Science", year="Third")
        Student.objects.update_or_create(email="student@virginia.edu", firstName="Bob", major="Computer Science", year="First")

    def test_store_message(self):
        request = self.factory.get('')
        request.user = self.user
        content = "This is a message!!"
        sender = Tutor.objects.get(email='tutor@virginia.edu').email + "tutor"
        receiver = Student.objects.get(email='student@virginia.edu').email + "student"

        response = store_message(request, content=content, sender=sender, receiver=receiver)
        self.assertEqual(response.status_code, 200)

        # check if message stored is same
        self.assertEqual(Message.objects.get(senderEmail=sender).msg_content, content)
        

# Written By: Soukarya
class GetMessageMineTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tutor', email='tutor@virginia.edu', password='top_secret')
        sender = "tutor@virginia.edututor"
        receiver = "student@virginia.edustudent"
        content = "This is a message!!"
        Message.objects.update_or_create(senderEmail=sender, recieverEmail=receiver, msg_content=content)

    def test_store_message_mine(self):
        request = self.factory.get('')
        request.user = self.user
        sender = "tutor@virginia.edututor"
        receiver = "student@virginia.edustudent"
        content = "This is a message!!"
        
        response = get_message(request, sender=sender, receiver=receiver)
        jsnResponse = json.loads(response.content)[0]

        self.assertEqual(jsnResponse['content'], content)
        self.assertEqual(jsnResponse['mine'], 1)

# Written By: Soukarya
class GetMessageNotMineTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tutor', email='tutor@virginia.edu', password='top_secret')
        sender = "tutor@virginia.edututor"
        receiver = "student@virginia.edustudent"
        content = "This is a message!!"
        Message.objects.update_or_create(senderEmail=sender, recieverEmail=receiver, msg_content=content)

    def test_store_message__mine(self):
        request = self.factory.get('')
        request.user = self.user
        sender = "tutor@virginia.edututor"
        receiver = "student@virginia.edustudent"
        content = "This is a message!!"
        
        response = get_message(request, sender=receiver, receiver=sender)
        jsnResponse = json.loads(response.content)[0]

        self.assertEqual(jsnResponse['content'], content)
        self.assertEqual(jsnResponse['mine'], 0)

# Written By: Soukarya
class MessageOrdering(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tutor', email='tutor@virginia.edu', password='top_secret')
        sender = "tutor@virginia.edututor"
        receiver = "student@virginia.edustudent"
        Message.objects.update_or_create(senderEmail=sender, recieverEmail=receiver, msg_content="#1")
        Message.objects.update_or_create(senderEmail=receiver, recieverEmail=sender, msg_content="#2")
        Message.objects.update_or_create(senderEmail=sender, recieverEmail=receiver, msg_content="#3")
        Message.objects.update_or_create(senderEmail=receiver, recieverEmail=sender, msg_content="#4")
        Message.objects.update_or_create(senderEmail=sender, recieverEmail=receiver, msg_content="#5")
        Message.objects.update_or_create(senderEmail=receiver, recieverEmail=sender, msg_content="#6")
        Message.objects.update_or_create(senderEmail=sender, recieverEmail=receiver, msg_content="#7")

    def test_store_message__mine(self):
        request = self.factory.get('')
        request.user = self.user
        sender = "tutor@virginia.edututor"
        receiver = "student@virginia.edustudent"
        
        response = get_message(request, sender=receiver, receiver=sender)
        jsnResponse = json.loads(response.content)

        self.assertEqual(jsnResponse[0]['content'], "#1")
        self.assertEqual(jsnResponse[1]['content'], "#2")
        self.assertEqual(jsnResponse[2]['content'], "#3")
        self.assertEqual(jsnResponse[3]['content'], "#4")
        self.assertEqual(jsnResponse[4]['content'], "#5")
        self.assertEqual(jsnResponse[5]['content'], "#6")
        self.assertEqual(jsnResponse[6]['content'], "#7")

# Written By: Soukarya
class MessageBothReceive(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tutor', email='tutor@virginia.edu', password='top_secret')
        Tutor.objects.update_or_create(email="tutor@virginia.edu", firstName="Bob", major="Computer Science", year="Third")
        Student.objects.update_or_create(email="student@virginia.edu", firstName="Bob", major="Computer Science", year="First")

    def test_store_message(self):
        request = self.factory.get('')
        request.user = self.user
        content = "This is a message!!"
        sender = Tutor.objects.get(email='tutor@virginia.edu').email + "tutor"
        receiver = Student.objects.get(email='student@virginia.edu').email + "student"

        response = store_message(request, content=content, sender=sender, receiver=receiver)
        self.assertEqual(response.status_code, 200)

        responseOne = json.loads(get_message(request, sender=receiver, receiver=sender).content)[0]
        responseTwo = json.loads(get_message(request, sender=sender, receiver=receiver).content)[0]

        self.assertNotEqual(responseOne['mine'], responseTwo['mine'])

# Written By: Soukarya
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class EditStudentPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Student.objects.update_or_create(email="student@virginia.edu", firstName="Bob", major="Computer Science", year="Third")
        self.user = User.objects.create_user(
            username='student', email='student@virginia.edu', password='top_secret')

    def test_details(self):
        request = self.factory.get('')
        request.user = self.user
        response = edit_student(request)
        self.assertEqual(response.status_code, 200)

# Written By: Soukarya
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class EditTutorPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Tutor.objects.update_or_create(email="tutor@virginia.edu", firstName="Bob", major="Computer Science", year="Third")
        self.user = User.objects.create_user(
            username='tutor', email='tutor@virginia.edu', password='top_secret')

    def test_details(self):
        request = self.factory.get('')
        request.user = self.user
        response = edit_tutor(request)
        self.assertEqual(response.status_code, 200)
