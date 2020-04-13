from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from QuickTutor.models import Student, Tutor, StudentRequest, TutorCourse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    return render(request, "QuickTutor/index.html", {})

@login_required
def student(request):
    currentUser = request.user
    email = currentUser.email

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        curr = Student.objects.get(email=email)
        curr.profile_image = myfile
        curr.save()

    try:
        # Returning students hit this branch
        currentStudent = Student.objects.get(email=email)

        # display the current requests the student has
        specificStudentRequestList = StudentRequest.objects.filter(studentEmail=email)

        session_num = len(StudentRequest.objects.all())
        tutors_online = len(Tutor.objects.all())
        

        return render(request, "QuickTutor/student.html",  {'student':currentStudent,'specificStudentRequestList': specificStudentRequestList, 
                                                            'session_num': session_num, 'tutors_online': tutors_online})
    except ObjectDoesNotExist:
        # First time students hit this branch

        # Block non-uva students
        # if email.split('@')[1] != "virginia.edu":
        #     return render(request, "QuickTutor/error.html", {})

        # redirect to a form to fill out name, major, etc.
        return render(request, "QuickTutor/signupStudent.html", {'email': email})


@login_required
def tutor(request):
    currentUser = request.user
    email = currentUser.email

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        curr = Tutor.objects.get(email=email)
        curr.profile_image = myfile
        curr.save()

    try:
        # Returning students hit this branch
        currentTutor = Tutor.objects.get(email=email)

        # list of all student requests
        studentRequestList = StudentRequest.objects.all()
        session_num = len(studentRequestList)
        tutors_online = len(Tutor.objects.all())

        return render(request, "QuickTutor/tutor.html", {'tutor': currentTutor, 'studentRequestList': studentRequestList, 'session_num': session_num, 'tutors_online': tutors_online})
    except ObjectDoesNotExist:
        # First time students hit this branch

        # Block non-uva students
        # if email.split('@')[1] != "virginia.edu":
        #     return render(request, "QuickTutor/error.html", {})

        # redirect to a form to fill out name, major, etc.
        return render(request, "QuickTutor/signupTutor.html", {'email': email})

@csrf_exempt
@login_required
def update_student(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        major = request.POST['major']
        year = request.POST['year']
        email = request.POST['email']

        Student.objects.update_or_create(email=email, username=email.split('@')[0], firstName=firstName, lastName=lastName, major=major, year=year)

    return HttpResponseRedirect(reverse('QuickTutor:student'))

@csrf_exempt
@login_required
def update_tutor(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        major = request.POST['major']
        year = request.POST['year']
        email = request.POST['email']
        
        obj, created = Tutor.objects.update_or_create(email=email, username=email.split('@')[0], firstName=firstName, lastName=lastName, major=major, year=year)
        
        myStr = "course" 
        x = 1
        temp = myStr + str(x)
        while temp in request.POST.keys():
            TutorCourse.objects.get_or_create(tutor=obj,course=request.POST[temp])
            x+=1
            temp = myStr + str(x)
       
       
    return HttpResponseRedirect(reverse('QuickTutor:tutor'))


@csrf_exempt
@login_required
def make_request(request):
    if request.method == "POST":
        # get student object of person requesting
        currentUser = request.user
        email = currentUser.email
        currentStudent = Student.objects.get(email=email)

        # update student table to be WAITING
        Student.objects.filter(email=email).update(status=1)

        # create a new row in studentRequests table
        courseName = request.POST['courseName']
        header = request.POST['header']

        description = request.POST['description']
        location = request.POST['location']
        confusion = request.POST['confusion']
        meetingDetails = request.POST['meetingDetails']

        obj, created = StudentRequest.objects.update_or_create(courseName=courseName, header=header, description=description, location=location, status=0,
        meetingDetails=meetingDetails, confusionMeter=confusion, studentEmail=currentStudent.email, studentUsername=currentStudent.email.split('@')[0])
        # RequestCourse.objects.get_or_create(request=obj,course=request.POST['subject'])
        
        return HttpResponseRedirect(reverse('QuickTutor:student'))


    return render(request, "QuickTutor/studentRequest.html", {})

@login_required
def accept(request, username):
    student = get_object_or_404(Student, username=username)
    student.accepted = 1
    student.status = 1
    stReq = StudentRequest.objects.get(studentEmail=student.email)
    currentUser = Tutor.objects.get(email=request.user.email)
    # currentUser.status = 1 # Brandie: changed this status to be 1 (meaning waiting for student to pick from list of tutors)
    currentUser.request = stReq
    currentUser.save(update_fields=['request', 'status'])
     
    #stReq.tutorEmail = currentUser.email
    #stReq.tutorUsername = currentUser.username
    student.save(update_fields=['status', 'accepted'])
    #stReq.save(update_fields=['tutorEmail', 'tutorUsername'])
    #sRequest = get_object_or_404(StudentRequest, studentUsername=username)
    return render(request, "QuickTutor/match.html", {'studentUsername': student.username, 'studentRequestHeader': stReq.header, 'currentUser': currentUser})
    #return HttpResponseRedirect(reverse('QuickTutor:accept', args=(user.username)))


@login_required
def cancel(request, studentUsername):
    studentRequest = StudentRequest.objects.get(studentUsername=studentUsername)

    student = Student.objects.get(email=studentRequest.studentEmail)
    student.status = 0
    student.save(update_fields=['status'])

    for tutor in studentRequest.tutor_set.all():
        tutor.status = 0
        tutor.save(update_fields=['status'])

    if studentRequest.tutorEmail != "":
        tutor = Student.objects.get(email=studentRequest.tutorEmail)
        tutor.status = 0
        tutor.save(update_fields=['status'])

    studentRequest.delete()

    return HttpResponseRedirect(reverse('QuickTutor:student'))


#code for the student to choose a tutor from the list of accepted tutors
@login_required
def studentsession(request, studentRequestHeader, tutorUsername):
    studentRequest = StudentRequest.objects.get(header=studentRequestHeader)
    studentUsername = request.user.username
    selectedTutor = Tutor.objects.get(username=tutorUsername)
    #set the selected tutor's status to be "accepted by student"
    selectedTutor.status =2
    selectedTutor.save(update_fields=['status'])
    #set the request's fields so that Greg's session page works!
    studentRequest.tutorEmail = selectedTutor.email
    studentRequest.tutorUsername = tutorUsername
    studentRequest.save(update_fields=['tutorEmail', 'tutorUsername'])


    #reset all the other tutor's statuses to be 0
    for tutor in studentRequest.tutor_set.all():
        if(tutor.username != tutorUsername):
            tutor.status = 0
            tutor.save(update_fields=['status'])

    #Greg's studentsession code:
    return render(request, "QuickTutor/studentsession.html", {'StudentRequest': studentRequest})


""" @login_required
def studentsession(request):
    currentUser = request.user
    email = currentUser.email
    currentStudent = Student.objects.get(email=email)
    studentRequest = StudentRequest.objects.get(studentUsername=currentStudent.username)
    return render(request, "QuickTutor/studentsession.html", {'StudentRequest': studentRequest}) """


@login_required
def tutorsession(request, studentRequestHeader, studentUsername):
    # currentUser = request.user
    # email = currentUser.email
    # currentTutor = Tutor.objects.get(email=email)
    # #studentRequest = StudentRequest.objects.get(tutorUsername=currentTutor.username)
    # studentRequest = currentTutor.request

    studentRequest = StudentRequest.objects.get(header=studentRequestHeader)
    return render(request, "QuickTutor/tutorsession.html", {'StudentRequest': studentRequest})


@login_required
def startsession(request):
    currentUser = request.user
    email = currentUser.email
    currentTutor = Tutor.objects.get(email=email)
    #studentRequest = StudentRequest.objects.get(tutorUsername=currentTutor.username)
    studentRequest = currentTutor.request
    studentRequest.status = 1 - studentRequest.status # this toggles right now, but should just be = 1 in the future
    studentRequest.save(update_fields=['status'])
    data = [{
    }]
    return JsonResponse(data, safe=False)

@login_required
def checkstart(request):
    currentUser = request.user
    email = currentUser.email
    currentStudent = Student.objects.get(email=email)
    studentRequest = StudentRequest.objects.get(studentUsername=currentStudent.username)
    data = [{
        'status': studentRequest.status
    }]
    return JsonResponse(data, safe=False)

@login_required
def checkaccepted(request):
    currentUser = request.user
    email = currentUser.email
    currentTutor = Tutor.objects.get(email=email)
    studentRequest = currentTutor.request
    studentAccepted = 0
    if (studentRequest.tutorEmail != ''):
        studentAccepted = 1
    data = [{
        'accepted': studentAccepted
    }]
    return JsonResponse(data, safe=False)

@login_required
def checkrequestcount(request):
    requestCount = len(StudentRequest.objects.all())
    data = [{
        'requestCount': requestCount
    }]
    return JsonResponse(data, safe=False)

@login_required
def checkacceptedtutorcount(request):
    currentStudent = request.user
    studentRequest = StudentRequest.objects.get(studentUsername=currentStudent.username)
    acceptedTutorCount = len(studentRequest.tutor_set.all())
    data = [{
        'acceptedTutorCount': acceptedTutorCount
    }]
    return JsonResponse(data, safe=False)

@csrf_exempt
@login_required
def tutorpostsession(request, studentRequestHeader, studentUsername):
    studentRequest = StudentRequest.objects.get(header=studentRequestHeader)
    if request.method == "POST":
        # get tutor object of person requesting and rating given
        currentUser = request.user
        email = currentUser.email
        selectedStudent = Student.objects.get(username=studentUsername)
        currentRating = selectedStudent.rating
        newRating = request.POST['rating']

        # update tutor status and request
        Tutor.objects.filter(email=email).update(status=0)
        Tutor.objects.filter(email=email).update(request='')

        # update student rating... not exactly a true average unfortunate
        if (currentRating != 0):
            selectedStudent.rating = (int(currentRating) + int(newRating))/2
        else:
            selectedStudent.rating = newRating
        selectedStudent.save(update_fields=['rating'])
        Student.objects.filter(username=studentUsername).update(status=0)
        Student.objects.filter(username=studentUsername).update(accepted=0)

        StudentRequest.objects.filter(header=studentRequestHeader).delete()

        return HttpResponseRedirect(reverse('QuickTutor:tutor'))

    return render(request, "QuickTutor/tutorpostsession.html", {'StudentRequest': studentRequest})

@csrf_exempt
@login_required
def studentpostsession(request, studentRequestHeader, tutorUsername):
    studentRequest = StudentRequest.objects.get(header=studentRequestHeader)
    return render(request, "QuickTutor/studentpostsession.html", {'StudentRequest': studentRequest, 'tutorUsername': tutorUsername})    

@login_required
def charge(request):
    if request.method == 'POST':
        # HANDLE PAYMENT
        amount = 500
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Paying the Tutor',
            source=request.POST['stripeToken']
        )

        currentUser = request.user
        email = currentUser.email
        req =StudentRequest.objects.get(studentEmail=email)

        student_payment = Student.objects.filter(email=email)
        tutor_payment = Tutor.objects.filter(email=req.tutorEmail)

        student_payment.update(balance=student_payment[0].balance-(amount/100))
        tutor_payment.update(balance=tutor_payment[0].balance+(amount/100))

        # HANDlE RATINGS AND COMPLAINTS
        # get student object of person requesting and rating given
        currentUser = request.user
        email = currentUser.email
        selectedTutor = Tutor.objects.get(username=request.POST['tutorUsername'])
        currentRating = selectedTutor.rating
        newRating = request.POST['rating']

        # update student status and accepted
        Student.objects.filter(email=email).update(status=0)
        Student.objects.filter(email=email).update(accepted=0)

        Tutor.objects.filter(username=request.POST['tutorUsername']).update(status=0)
        Tutor.objects.filter(username=request.POST['tutorUsername']).update(request='')

        # update tutor rating... not exactly a true average
        if (currentRating != 0):
            selectedTutor.rating = (int(currentRating) + int(newRating))/2
        else:
            selectedTutor.rating = newRating
        selectedTutor.save(update_fields=['rating'])

        # delete the request
        StudentRequest.objects.filter(header=request.POST['header']).delete()

        return HttpResponseRedirect(reverse('QuickTutor:student'))