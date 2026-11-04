
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student, Teacher, Attendance, Marks


# ================= DASHBOARD =================

@login_required
def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_attendance': Attendance.objects.count(),
        'total_marks': Marks.objects.count(),
    }
    return render(request, 'dashboard.html', context)


# ================= STUDENT MANAGEMENT =================

@login_required
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST.get('student_id'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            date_of_birth=request.POST.get('date_of_birth'),
            gender=request.POST.get('gender'),
            course=request.POST.get('course'),
            department=request.POST.get('department'),
            address=request.POST.get('address'),
        )
        messages.success(request, 'Student added successfully!')
        return redirect('student_list')

    return render(request, 'add_student.html')


@login_required
def student_list(request):
    search_query = request.GET.get('search', '')
    students = Student.objects.all()

    if search_query:
        students = students.filter(
            Q(student_id__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    return render(request, 'student_list.html', {
        'students': students.order_by('-id'),
        'search_query': search_query,
    })


@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.student_id = request.POST.get('student_id')
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.gender = request.POST.get('gender')
        student.course = request.POST.get('course')
        student.department = request.POST.get('department')
        student.address = request.POST.get('address')

        student.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})


# ================= TEACHER MANAGEMENT =================

@login_required
def add_teacher(request):
    if request.method == 'POST':
        Teacher.objects.create(
            teacher_id=request.POST.get('teacher_id'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            department=request.POST.get('department'),
            joining_date=request.POST.get('joining_date'),
        )
        messages.success(request, 'Teacher added successfully!')
        return redirect('teacher_list')

    return render(request, 'add_teacher.html')


@login_required
def teacher_list(request):
    search_query = request.GET.get('search', '')
    teachers = Teacher.objects.all()

    if search_query:
        teachers = teachers.filter(
            Q(teacher_id__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(subject__icontains=search_query)
        )

    return render(request, 'teacher_list.html', {
        'teachers': teachers.order_by('-id'),
        'search_query': search_query,
    })


@login_required
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.teacher_id = request.POST.get('teacher_id')
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.email = request.POST.get('email')
        teacher.phone = request.POST.get('phone')
        teacher.subject = request.POST.get('subject')
        teacher.department = request.POST.get('department')
        teacher.joining_date = request.POST.get('joining_date')

        teacher.save()
        messages.success(request, 'Teacher updated successfully!')
        return redirect('teacher_list')

    return render(request, 'edit_teacher.html', {'teacher': teacher})


@login_required
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted successfully!')
        return redirect('teacher_list')

    return render(request, 'delete_teacher.html', {'teacher': teacher})


# ================= ATTENDANCE MANAGEMENT =================

@login_required
def add_attendance(request):
    students = Student.objects.all().order_by('first_name')

    if request.method == 'POST':
        student = get_object_or_404(Student, id=request.POST.get('student'))
        attendance_date = request.POST.get('date')
        status = request.POST.get('status')

        if status not in ['Present', 'Absent', 'Late']:
            messages.error(request, 'Invalid attendance status!')
            return redirect('add_attendance')

        Attendance.objects.update_or_create(
            student=student,
            date=attendance_date,
            defaults={'status': status}
        )

        messages.success(request, 'Attendance saved successfully!')
        return redirect('attendance_list')

    return render(request, 'add_attendance.html', {'students': students})


@login_required
def attendance_list(request):
    attendance_records = Attendance.objects.select_related(
        'student'
    ).all().order_by('-date')

    return render(request, 'attendance_list.html', {
        'attendance_records': attendance_records
    })


# ================= MARKS MANAGEMENT =================

@login_required
def add_marks(request):
    students = Student.objects.all().order_by('first_name')

    if request.method == 'POST':
        student = get_object_or_404(Student, id=request.POST.get('student'))

        try:
            total_marks = int(request.POST.get('total_marks'))
            obtained_marks = int(request.POST.get('obtained_marks'))
        except (TypeError, ValueError):
            messages.error(request, 'Please enter valid marks!')
            return redirect('add_marks')

        if (
            total_marks <= 0 or
            obtained_marks < 0 or
            obtained_marks > total_marks
        ):
            messages.error(request, 'Please enter valid marks!')
            return redirect('add_marks')

        Marks.objects.create(
            student=student,
            subject=request.POST.get('subject'),
            total_marks=total_marks,
            obtained_marks=obtained_marks,
            exam_date=request.POST.get('exam_date')
        )

        messages.success(request, 'Marks added successfully!')
        return redirect('marks_list')

    return render(request, 'add_marks.html', {'students': students})


@login_required
def marks_list(request):
    marks_records = Marks.objects.select_related(
        'student'
    ).all().order_by('-exam_date')

    return render(request, 'marks_list.html', {
        'marks_records': marks_records
    })


# ================= RESULTS & REPORTS =================

@login_required
def student_results(request):
    students = Student.objects.all().order_by('first_name')
    results = []

    for student in students:
        marks_records = Marks.objects.filter(student=student)

        total_obtained = sum(
            record.obtained_marks for record in marks_records
        )

        total_marks = sum(
            record.total_marks for record in marks_records
        )

        percentage = (
            (total_obtained / total_marks) * 100
            if total_marks > 0 else 0
        )

        if total_marks == 0:
            grade = 'N/A'
        elif percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 40:
            grade = 'D'
        else:
            grade = 'F'

        attendance_records = Attendance.objects.filter(student=student)
        total_days = attendance_records.count()
        present_days = attendance_records.filter(
            status='Present'
        ).count()

        attendance_percentage = (
            (present_days / total_days) * 100
            if total_days > 0 else 0
        )

        results.append({
            'student': student,
            'total_obtained': total_obtained,
            'total_marks': total_marks,
            'percentage': round(percentage, 2),
            'grade': grade,
            'attendance_percentage': round(attendance_percentage, 2),
        })

    return render(request, 'student_results.html', {
        'results': results
    })
