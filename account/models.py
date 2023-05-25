from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, get_object_or_404

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_lecturer = models.BooleanField('Is lecturer', default=False)
    is_student = models.BooleanField('Is student', default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_lecturer:
            Lecturer.objects.get_or_create(user=self)
        if self.is_student:
            Student.objects.get_or_create(user=self)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
    matriculation_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    other_biodata_fields = models.TextField()

class Course(models.Model):
    course_year = models.CharField(max_length=10)  # 1.Year, 2.Year, 3.Year, 4.Year
    department_name = models.CharField(max_length=30)  # Computer Engineering
    course_id = models.CharField(max_length=10)  # CME4401
    course_name = models.TextField()  # Applications of Decision Support Systems
    theoretical_hour = models.IntegerField()  # 2 hours
    practical_hour = models.IntegerField()  # 2 hours
    branch = models.CharField(max_length=20)  # 1 or 2. branch
    credit = models.IntegerField()  # 3 credits
    akts = models.IntegerField()  # 6 AKTS
    course_type = models.CharField(max_length=10)  # compulsory or elective
    is_course_chosen = models.BooleanField(default=False)  # True or False
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return f"{self.course_id} - {self.course_name}"

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='lecturer')
    employee_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    other_biodata_fields = models.TextField()
    courses = models.ManyToManyField(Course, related_name='lecturers')

    def __str__(self):
        return self.full_name


