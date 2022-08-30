from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ('name', '')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'