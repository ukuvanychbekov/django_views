from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    mentor_name = models.CharField(max_length=100)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    laptop = models.CharField(max_length=100)

    def __str__(self):
        return self.name