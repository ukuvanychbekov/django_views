from django.shortcuts import render, redirect
from .models import Course, Student
from django.http import HttpResponse
from .form import CourseForm, StudentForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses':courses})


def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Error')
        # name = request.GET.get('name')
        # mentor_name = request.GET.get('mentor_name')
        # language = request.GET.get('language')
        # if name and mentor_name and language:
        #     course = Course.objects.create(name=name, mentor_name=mentor_name, language=language)
        # return HttpResponse('Done!')
    if request.method == 'GET':
        form = CourseForm()
        return render(request, 'course_add.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students':students})


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return HttpResponse('Error')
    if request.method == 'GET':
        form = StudentForm()
        return render(request, 'student_add.html', {'form': form})



