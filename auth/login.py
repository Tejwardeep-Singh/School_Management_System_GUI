import tkinter as tk
from tkinter import messagebox
from db import connect_db

def open_login(role):
    window = tk.Toplevel()
    window.title(f"{role} Login")
    window.geometry("300x250")

    tk.Label(window, text=f"{role} Login", font=("Arial", 14)).pack(pady=10)

    tk.Label(window, text="User ID").pack()
    user_entry = tk.Entry(window)
    user_entry.pack()

    tk.Label(window, text="Password").pack()
    pass_entry = tk.Entry(window, show="*")
    pass_entry.pack()

    def authenticate():
        user = user_entry.get()
        password = pass_entry.get()

        # HEAD LOGIN (hardcoded for now)
        if role == "Head":
            if user == "sohan singh" and password == "school123":
                messagebox.showinfo("Success", "Head Login Successful")
                from head.head_dashboard import open_head_dashboard
                open_head_dashboard()
            else:
                messagebox.showerror("Error", "Invalid Credentials")

        # TEACHER LOGIN (DB)
        elif role == "Teacher":
            conn = connect_db()
            cursor = conn.cursor()

            query = "SELECT * FROM teacher WHERE user_id=%s AND password=%s"
            cursor.execute(query, (user, password))

            result = cursor.fetchone()
            conn.close()

            if result:
                from teacher.teacher_dashboard import open_teacher_dashboard
                window.destroy() 
                open_teacher_dashboard(int(user))
            else:
                messagebox.showerror("Error", "Invalid Credentials")

        # STUDENT LOGIN (DB)
        elif role == "Student":
            conn = connect_db()
            cursor = conn.cursor()

            # TEMP: using class_1 table
            query = "SELECT * FROM class_1 WHERE ref_id=%s AND password=%s"
            cursor.execute(query, (int(user), int(password)))

            result = cursor.fetchone()
            conn.close()

            if result:
                from student.student_dashboard import open_student_dashboard
                open_student_dashboard(int(user), "class_1")
            else:
                messagebox.showerror("Error", "Invalid Credentials")

    tk.Button(window, text="Login", command=authenticate).pack(pady=15)