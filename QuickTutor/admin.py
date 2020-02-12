from django.contrib import admin

from .models import Student, Tutor, studentRequest

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(studentRequest)