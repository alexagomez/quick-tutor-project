from django.contrib import admin

from .models import Student, Tutor, StudentRequest, RequestCourse, TutorCourse

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(StudentRequest)
admin.site.register(TutorCourse)
admin.site.register(RequestCourse)

