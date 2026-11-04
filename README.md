# 🎓 Student Management System

A web-based **Student Management System** developed using Python, Django, MySQL, HTML, CSS, and Bootstrap. This application helps educational institutions manage student records, teacher information, attendance, marks, and academic reports efficiently.

## 📌 Project Overview

The Student Management System is designed to simplify academic record management. It provides a user-friendly dashboard where authorized users can manage student and teacher details, track attendance, maintain examination marks, and generate reports.

## ✨ Features

- 🔐 **User Authentication** – Secure login and logout functionality.
- 📊 **Dashboard** – View student, teacher, attendance, and marks statistics.
- 👨‍🎓 **Student Management** – Add, view, edit, and delete student records.
- 👨‍🏫 **Teacher Management** – Manage teacher information.
- 📅 **Attendance Management** – Record and view student attendance.
- 📝 **Marks Management** – Add and view examination marks.
- 📈 **Results & Reports** – Calculate student percentages and grades.
- 📄 **PDF Export** – Download student information as PDF.
- 📊 **Excel Export** – Export student records to Excel.
- 🗄️ **MySQL Database** – Store and manage application data.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| MySQL | Database |
| HTML5 | Web page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive user interface |
| JavaScript | Frontend interactions |
| OpenPyXL | Excel report generation |
| ReportLab | PDF report generation |

## 📂 Project Structure

```text
Student-Management-System/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── reports.py
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── student_list.html
│   ├── teacher_list.html
│   ├── attendance_list.html
│   ├── marks_list.html
│   └── student_results.html
│
├── static/
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Prabhat-2004/Student-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Student-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows Git Bash:**

```bash
source venv/Scripts/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a template.

Add your own configuration:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DB_NAME=student_management
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
```

**Important:** Never upload your `.env` file or real passwords to GitHub.

### 7. Create the MySQL Database

Open MySQL and execute:

```sql
CREATE DATABASE student_management;
```

### 8. Apply Migrations

```bash
python manage.py migrate
```

### 9. Create an Admin Account

```bash
python manage.py createsuperuser
```

Follow the instructions to create your username and password.

### 10. Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## 🔑 Admin Panel

Access the Django administration panel at:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser account you created.

## 📊 Main Modules

| Module | Description |
|---|---|
| Dashboard | Displays system statistics |
| Students | Manages student information |
| Teachers | Manages teacher information |
| Attendance | Tracks student attendance |
| Marks | Stores examination marks |
| Results | Displays percentages and grades |
| Reports | Downloads PDF and Excel reports |

## 🎯 Project Objectives

- To reduce manual student record management.
- To make academic information easier to access.
- To improve attendance and examination record management.
- To generate reports quickly and efficiently.
- To provide a simple and user-friendly management system.

## 🚀 Future Improvements

- Student profile pictures.
- Search and filter functionality.
- Student and teacher profile pages.
- Email notifications.
- Role-based access for administrators and teachers.

## 👨‍💻 Developer

**Prabhat Dakua**

- GitHub: [Prabhat-2004](https://github.com/Prabhat-2004)
- Project: [Student Management System](https://github.com/Prabhat-2004/Student-Management-System)

---

⭐ If you find this project useful, consider giving it a star!

**Developed with Python and Django.**
