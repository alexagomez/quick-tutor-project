from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

app_name = 'QuickTutor'
urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('tutor', views.tutor, name='tutor'),
    path('update_student', views.update_student, name='update_student'),
    path('update_tutor', views.update_tutor, name='update_tutor'),
    path('edit_student', views.edit_student, name='edit_student'),
    path('edit_tutor', views.edit_tutor, name='edit_tutor'),
    path('make_request', views.make_request, name='make_request'),
    path('match/<username>/', views.accept, name='accept'),
    path('cancel/<studentUsername>/', views.cancel, name='cancel'),
    path('tutorsession/<studentRequestHeader>/<studentUsername>/', views.tutorsession, name='tutorsession'),
    path('studentsession/<studentRequestHeader>/<tutorUsername>/', views.studentsession, name='studentsession'),
    path('startsession', views.startsession, name='startsession'),
    path('checkstart', views.checkstart, name='checkstart'),
    path('checkaccepted', views.checkaccepted, name='checkaccepted'),
    path('checkrequestcount', views.checkrequestcount, name='checkrequestcount'),
    path('checkacceptedtutorcount', views.checkacceptedtutorcount, name='checkacceptedtutorcount'),
    path('checksessionstudent', views.checksessionstudent, name='checksessionstudent'),
    path('tutorpostsession/<studentRequestHeader>/<studentUsername>/', views.tutorpostsession, name='tutorpostsession'),
    path('studentpostsession/<studentRequestHeader>/<tutorUsername>/', views.studentpostsession, name='studentpostsession'),
    path('charge', views.charge, name='charge'),
    path('about', views.about, name='about'),
    path('store_message/<content>/<sender>/<receiver>/', views.store_message, name='store_message'),
    path('get_message/<sender>/<receiver>/', views.get_message, name='get_message'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


