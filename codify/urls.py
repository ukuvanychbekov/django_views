from django.urls import path
from . import views


urlpatterns = [
    path('course/list/', views.course_list, name='course_list'),
    path('course/add/', views.course_add, name='course_add'),
    path('student/list/', views.student_list, name='student_list'),
    path('student/add/', views.student_add, name='student_add'),
]