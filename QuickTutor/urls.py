from django.urls import path
from . import views

app_name = 'QuickTutor'
urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('tutor', views.tutor, name='tutor'),
    path('update_student', views.update_student, name='update_student'),
    path('update_tutor', views.update_tutor, name='update_tutor'),
    path('make_request', views.make_request, name='make_request'),
    path('match/<username>/', views.accept, name='accept'),
]

