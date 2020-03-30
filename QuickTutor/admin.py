from django.contrib import admin

from .models import Student, Tutor, StudentRequest, TutorCourse

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(StudentRequest)
admin.site.register(TutorCourse)

