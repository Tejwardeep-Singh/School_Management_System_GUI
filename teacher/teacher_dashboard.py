import tkinter as tk
from tkinter import messagebox, ttk
from db import connect_db

# 🎨 THEME
BG = "#0f172a"
SIDEBAR = "#020617"
CARD = "#1e293b"
BTN = "#3b82f6"
TEXT = "#f8fafc"

# ================= DASHBOARD =================
def open_teacher_dashboard(user_id):
    window = tk.Toplevel()
    window.title("Teacher Dashboard")
    window.geometry("900x500")
    window.configure(bg=BG)

    # ===== SIDEBAR =====
    sidebar = tk.Frame(window, bg=SIDEBAR, width=200)
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="Teacher Panel",
             bg=SIDEBAR, fg=TEXT,
             font=("Segoe UI", 16, "bold")).pack(pady=20)

    def sidebar_btn(text, cmd):
        btn = tk.Button(
            sidebar,
            text=text,
            command=cmd,
            bg=SIDEBAR,
            fg=TEXT,
            font=("Segoe UI", 10),
            bd=0,
            cursor="hand2",
            pady=10
        )

        # 🔥 Hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg=BTN))
        btn.bind("<Leave>", lambda e: btn.config(bg=SIDEBAR))

        return btn

    sidebar_btn("Profile", lambda: view_profile(user_id)).pack(fill="x")
    sidebar_btn("Apply Leave", lambda: apply_leave(user_id)).pack(fill="x")
    sidebar_btn("Salary", lambda: view_salary(user_id)).pack(fill="x")
    sidebar_btn("Students", view_students).pack(fill="x")

    # ===== MAIN AREA =====
    main = tk.Frame(window, bg=BG)
    main.pack(side="right", fill="both", expand=True)

    tk.Label(main, text="Welcome Back 👋",
             bg=BG, fg=TEXT,
             font=("Segoe UI", 20, "bold")).pack(pady=20)

    # ===== CARDS =====
    card_frame = tk.Frame(main, bg=BG)
    card_frame.pack()

    def card(title):
        frame = tk.Frame(card_frame, bg=CARD, width=180, height=100)
        frame.pack(side="left", padx=15, pady=10)
        frame.pack_propagate(False)

        tk.Label(frame, text=title,
                 bg=CARD, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(expand=True)

    card("Profile")
    card("Leave")
    card("Salary")
    card("Students")


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
    window.geometry("350x300")
    window.configure(bg=BG)

    frame = tk.Frame(window, bg=CARD, padx=20, pady=20)
    frame.pack(pady=30)

    tk.Label(frame, text="Apply Leave",
             bg=CARD, fg=TEXT,
             font=("Segoe UI", 14, "bold")).pack(pady=10)

    from_date = tk.Entry(frame)
    from_date.pack(pady=5)

    to_date = tk.Entry(frame)
    to_date.pack(pady=5)

    reason = tk.Entry(frame)
    reason.pack(pady=5)

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

    tk.Button(frame, text="Submit",
              bg=BTN, fg="white",
              width=15,
              command=submit).pack(pady=10)


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
    window.geometry("600x400")
    window.configure(bg=BG)

    style = ttk.Style()
    style.theme_use("default")

    style.configure("Treeview",
                    background=CARD,
                    foreground="white",
                    fieldbackground=CARD,
                    rowheight=25)

    style.configure("Treeview.Heading",
                    background=BTN,
                    foreground="white")

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