from django.urls import path
from . import views


urlpatterns = [
    path('course/list/', views.course_list_api, name='course_list_api'),
    # path('course/add/', views.course_add, name='course_add')
]