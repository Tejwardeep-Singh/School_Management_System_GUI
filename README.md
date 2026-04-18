# 🏫 School Management System (Tkinter + MySQL)

## 📌 Overview

This project is a **GUI-based School Management System** built using **Python (Tkinter)** and **MySQL**.
It is an upgraded version of my Class 12 project (originally CLI-based), now redesigned with a graphical interface for better usability and structure.

The system helps manage:

* Students
* Teachers
* Leave requests
* School records

---

## 🚀 Features

### 🔐 Authentication System

* Head Login
* Staff Login
* Student Login

### 👨‍🏫 Head Panel

* View student records
* Add new students
* Manage leave requests
* Access school data

### 👨‍🎓 Student Module

* View student details
* Add student records

### 🧑‍🏫 Teacher Module *(planned / extendable)*

* View teacher details
* Manage staff data

---

## 🛠️ Tech Stack

* **Frontend (GUI):** Tkinter (Python)
* **Backend Logic:** Python
* **Database:** MySQL
* **Connector:** mysql-connector-python

---

## 📂 Project Structure

```
school_gui/
│
├── main.py                # Entry point
├── db.py                  # Database connection
│
├── head/
│   └── head_dashboard.py  # Head panel UI
│
├── student/
│   ├── view_student.py    # View students (table)
│   └── add_student.py     # Add student form
│
├── teacher/
│   └── view_teacher.py    # (optional / future)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/school-gui.git
cd school-gui
```

---

### 2️⃣ Install Dependencies

```
pip install mysql-connector-python
```

---

### 3️⃣ Setup MySQL Database

* Create a database named `school`
* Import or create required tables (students, teachers, etc.)

Update your credentials in `db.py`:

```python
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="school"
    )
```

---

### 4️⃣ Run the Application

```
python main.py
```

---

## 📸 Application Flow

1. Launch application
2. Choose login type
3. Access dashboard
4. Perform operations (view/add/manage data)

---

## 🔮 Future Improvements

* 🔐 Secure authentication system
* 🌐 Connect with remote database / API
* 🎨 Improved UI design (themes, layouts)
* 📊 Dashboard with analytics
* 🔄 Integration with web app (Pandori)

---

## 🧠 Learning Outcomes

Through this project, I learned:

* GUI development using Tkinter
* Database integration with Python
* Modular code structure
* Transition from CLI → GUI applications

---

## 📌 Author

**Tejwardeep Singh**
B.Tech CSE (2024–2028)

---

## ⭐ Note

This project is part of my learning journey:

* Started as a **Class 12 Python + SQL project (CLI)**
* Now upgraded into a **GUI-based desktop application**
* Will be further scaled into a **full-stack system**

---

## 💬 Feedback

Feel free to suggest improvements or contribute to the project!
