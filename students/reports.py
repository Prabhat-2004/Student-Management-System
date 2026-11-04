
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone

from openpyxl import Workbook
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from .models import Student


@login_required
def export_students_excel(request):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Students"

    headers = [
        "Student ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Course",
        "Department",
        "Admission Date",
    ]

    sheet.append(headers)

    students = Student.objects.all().order_by("student_id")

    for student in students:
        sheet.append([
            student.student_id,
            student.first_name,
            student.last_name,
            student.email,
            student.phone,
            student.course,
            student.department,
            student.admission_date.strftime("%Y-%m-%d")
            if student.admission_date else "",
        ])

    for cell in sheet[1]:
        cell.font = cell.font.copy(bold=True, color="FFFFFF")
        cell.fill = cell.fill.copy(
            fill_type="solid",
            fgColor="172554"
        )

    for column in sheet.columns:
        max_length = max(len(str(cell.value or "")) for cell in column)
        sheet.column_dimensions[column[0].column_letter].width = max_length + 4

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="students_report.xlsx"'

    workbook.save(response)
    return response


@login_required
def export_students_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="students_report.pdf"'

    document = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=25,
        leftMargin=25,
        topMargin=30,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()
    elements = []

    elements.append(
        Paragraph("Student Management System", styles["Title"])
    )
    elements.append(
        Paragraph("Student Records Report", styles["Heading2"])
    )
    elements.append(
        Paragraph(
            f"Generated on: {timezone.localtime().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )
    elements.append(Spacer(1, 20))

    data = [[
        "Student ID",
        "Name",
        "Email",
        "Phone",
        "Course",
        "Department",
    ]]

    students = Student.objects.all().order_by("student_id")

    for student in students:
        data.append([
            str(student.student_id),
            f"{student.first_name} {student.last_name}",
            str(student.email),
            str(student.phone),
            str(student.course),
            str(student.department),
        ])

    table = Table(
        data,
        repeatRows=1,
        colWidths=[75, 110, 170, 90, 100, 110]
    )

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#172554")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [
            colors.white,
            colors.HexColor("#EFF6FF")
        ]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.append(table)
    document.build(elements)

    return response
