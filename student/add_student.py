import tkinter as tk
from db import connect_db

def add_student():
    window = tk.Toplevel()
    window.title("Add Student")

    tk.Label(window, text="Name").pack()
    name = tk.Entry(window)
    name.pack()

    tk.Label(window, text="Class").pack()
    student_class = tk.Entry(window)
    student_class.pack()

    def save():
        conn = connect_db()
        cursor = conn.cursor()

        query = "INSERT INTO class_1 (name) VALUES (%s)"
        cursor.execute(query, (name.get(),))

        conn.commit()
        conn.close()

        print("Saved")

    tk.Button(window, text="Save", command=save).pack(pady=10)