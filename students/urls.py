
from django.urls import path
from . import views
from . import reports

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Student Management
    path('add-student/', views.add_student, name='add_student'),
    path('students/', views.student_list, name='student_list'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),

    # Teacher Management
    path('add-teacher/', views.add_teacher, name='add_teacher'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),

    # Attendance Management
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('attendance/', views.attendance_list, name='attendance_list'),

    # Marks Management
    path('add-marks/', views.add_marks, name='add_marks'),
    path('marks/', views.marks_list, name='marks_list'),

    # Results
    path('results/', views.student_results, name='student_results'),

    # Export Reports
    path('export/students/excel/', reports.export_students_excel, name='export_students_excel'),
    path('export/students/pdf/', reports.export_students_pdf, name='export_students_pdf'),
]
