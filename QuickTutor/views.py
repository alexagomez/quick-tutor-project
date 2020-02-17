from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from QuickTutor.models import Student, Tutor, studentRequest


def index(request):
    return render(request, "QuickTutor/index.html", {})

@login_required
def student(request):
    currentUser = request.user
    email = currentUser.email
    try:
        # Returning students hit this branch
        currentStudent = Student.objects.get(email=email)

        return render(request, "QuickTutor/student.html",  {'student':currentStudent,})
    except ObjectDoesNotExist:
        # First time students hit this branch


        # Block non-uva students
        if email.split('@')[1] != "virginia.edu":
            return render(request, "QuickTutor/error.html", {})

        # redirect to a form to fill out name, major, etc.
        return render(request, "QuickTutor/signupStudent.html", {'email': email})


@login_required
def tutor(request):
    currentUser = request.user
    email = currentUser.email
    try:
        # Returning students hit this branch
        currentTutor = Tutor.objects.get(email=email)

        return render(request, "QuickTutor/tutor.html", {'tutor': currentTutor})
    except ObjectDoesNotExist:
        # First time students hit this branch

        # Block non-uva students
        if email.split('@')[1] != "virginia.edu":
            return render(request, "QuickTutor/error.html", {})

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

        Student.objects.update_or_create(email=email, firstName=firstName, lastName=lastName, major=major, year=year)

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

        Tutor.objects.update_or_create(email=email, firstName=firstName, lastName=lastName, major=major, year=year)


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
        subject = request.POST['subject']
        description = request.POST['description']
        location = request.POST['location']
        confusion = request.POST['confusion']

        studentRequest.objects.update_or_create(courseName=courseName, 
        subject=subject, description=description, location=location, 
        confusionMeter=confusion, studentID=currentStudent.ID)
        
        
        return HttpResponseRedirect(reverse('QuickTutor:student'))


    return render(request, "QuickTutor/studentRequest.html", {})