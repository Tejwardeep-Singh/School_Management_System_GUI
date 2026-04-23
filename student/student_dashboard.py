import tkinter as tk
from tkinter import messagebox
from db import connect_db

# ================= DASHBOARD =================
def open_student_dashboard(student_id, student_class):
    window = tk.Toplevel()
    window.title("Student Dashboard")
    window.geometry("400x300")

    tk.Label(window, text="Student Panel", font=("Arial", 16)).pack(pady=20)

    tk.Button(window, text="View Profile", width=25,
              command=lambda: view_profile(student_id, student_class)).pack(pady=10)

    tk.Button(window, text="Apply Leave", width=25,
              command=lambda: apply_leave(student_id)).pack(pady=10)


# ================= VIEW PROFILE =================
def view_profile(student_id, student_class):
    conn = connect_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM {student_class} WHERE ref_id=%s"
    cursor.execute(query, (student_id,))
    data = cursor.fetchone()

    conn.close()

    if data:
        messagebox.showinfo("Profile", f"""
Name: {data[3]}
Father: {data[4]}
Class: {data[5]}
Address: {data[6]}
Mobile: {data[7]}
""")
    else:
        messagebox.showerror("Error", "No data found")


# ================= APPLY LEAVE =================
def apply_leave(student_id):
    window = tk.Toplevel()
    window.title("Apply Leave")

    tk.Label(window, text="From Date (YYYY-MM-DD)").pack()
    from_date = tk.Entry(window)
    from_date.pack()

    tk.Label(window, text="To Date (YYYY-MM-DD)").pack()
    to_date = tk.Entry(window)
    to_date.pack()

    tk.Label(window, text="Reason").pack()
    reason = tk.Entry(window)
    reason.pack()

    def submit():
        conn = connect_db()
        cursor = conn.cursor()

        query = """
        INSERT INTO leave_request_student
        (name, ref_id, from_date, to_date, reason, status)
        VALUES (%s, %s, %s, %s, %s, 'pending')
        """

        # get student name
        cursor.execute("SELECT name FROM class_1 WHERE ref_id=%s", (student_id,))
        student = cursor.fetchone()

        if student:
            cursor.execute(query, (
                student[0],
                student_id,
                from_date.get(),
                to_date.get(),
                reason.get()
            ))

            conn.commit()
            messagebox.showinfo("Success", "Leave Applied")

        conn.close()

    tk.Button(window, text="Submit", command=submit).pack(pady=10)