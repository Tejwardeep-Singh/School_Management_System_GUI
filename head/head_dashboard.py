import tkinter as tk
from student.view_student import view_students

def open_head_dashboard():
    window = tk.Toplevel()
    window.title("Head Dashboard")
    window.geometry("500x400")

    tk.Label(window, text="Head Panel", font=("Arial", 16)).pack(pady=20)

    tk.Button(window, text="View Students", command=view_students).pack(pady=10)
    tk.Button(window, text="Add Student").pack(pady=10)
    tk.Button(window, text="Leave Requests").pack(pady=10)