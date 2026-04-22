import tkinter as tk
from tkinter import messagebox, ttk
from db import connect_db

# ================= DASHBOARD =================
def open_teacher_dashboard(user_id):
    window = tk.Toplevel()
    window.title("Teacher Dashboard")
    window.geometry("500x400")

    tk.Label(window, text="Teacher Panel", font=("Arial", 16)).pack(pady=20)

    tk.Button(window, text="View Profile", width=25,
              command=lambda: view_profile(user_id)).pack(pady=10)

    tk.Button(window, text="Apply Leave", width=25,
              command=lambda: apply_leave(user_id)).pack(pady=10)

    tk.Button(window, text="View Salary", width=25,
              command=lambda: view_salary(user_id)).pack(pady=10)

    tk.Button(window, text="View Students", width=25,
              command=view_students).pack(pady=10)


# ================= VIEW PROFILE =================
def view_profile(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM teacher WHERE user_id=%s", (user_id,))
    data = cursor.fetchone()

    conn.close()

    if data:
        messagebox.showinfo("Profile", f"""
Name: {data[3]}
Designation: {data[4]}
Age: {data[5]}
Salary: {data[6]}
""")
    else:
        messagebox.showerror("Error", "No data found")


# ================= APPLY LEAVE =================
def apply_leave(user_id):
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

        cursor.execute("SELECT name, ref_id FROM teacher WHERE user_id=%s", (user_id,))
        teacher = cursor.fetchone()

        if teacher:
            cursor.execute("""
                INSERT INTO leave_request_teacher
                (name, ref_id, from_date, to_date, reason, status)
                VALUES (%s, %s, %s, %s, %s, 'pending')
            """, (teacher[0], teacher[1], from_date.get(), to_date.get(), reason.get()))

            conn.commit()
            messagebox.showinfo("Success", "Leave Applied")

        conn.close()

    tk.Button(window, text="Submit", command=submit).pack(pady=10)


# ================= VIEW SALARY =================
def view_salary(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT ref_id FROM teacher WHERE user_id=%s", (user_id,))
    ref = cursor.fetchone()

    if ref:
        cursor.execute("SELECT * FROM payroll WHERE ref_id=%s", (ref[0],))
        data = cursor.fetchone()

        if data:
            messagebox.showinfo("Salary", f"""
Basic Salary: {data[2]}
Increment: {data[3]}
Tax: {data[4]}
Gross: {data[5]}
""")
        else:
            messagebox.showerror("Error", "No salary record found")

    conn.close()


# ================= VIEW STUDENTS =================
def view_students():
    window = tk.Toplevel()
    window.title("Students")

    tree = ttk.Treeview(window, columns=("ID", "Name"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.pack(fill="both", expand=True)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT ref_id, name FROM class_1")

    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    conn.close()