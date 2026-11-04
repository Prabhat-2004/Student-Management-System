
from django.db import models


# Student Model
class Student(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    admission_date = models.DateField(auto_now_add=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"


# Teacher Model
class Teacher(models.Model):

    teacher_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.teacher_id} - {self.first_name} {self.last_name}"


# Attendance Model
class Attendance(models.Model):

    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.student_id} - {self.date} - {self.status}"


# Marks Model
class Marks(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='marks_records'
    )

    subject = models.CharField(max_length=100)
    total_marks = models.PositiveIntegerField(default=100)
    obtained_marks = models.PositiveIntegerField()
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.student.student_id} - {self.subject}"
