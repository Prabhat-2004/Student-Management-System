from django.contrib import admin
from .models import Student, Teacher, Attendance, Marks


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'first_name',
        'last_name',
        'email',
        'course',
        'department',
    )
    search_fields = (
        'student_id',
        'first_name',
        'last_name',
        'email',
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'teacher_id',
        'first_name',
        'last_name',
        'email',
        'subject',
        'department',
    )
    search_fields = (
        'teacher_id',
        'first_name',
        'last_name',
        'email',
    )


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('status', 'date')


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'total_marks',
        'obtained_marks',
        'exam_date',
    )
    search_fields = ('subject',)