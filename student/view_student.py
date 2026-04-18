import tkinter as tk
from tkinter import ttk
from db import connect_db

def view_students():
    window = tk.Toplevel()
    window.title("Students")

    tree = ttk.Treeview(window, columns=("ID", "Name"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")

    tree.pack(fill="both", expand=True)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT ref_id, name FROM class_1")  # temporary

    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    conn.close()