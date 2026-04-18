import tkinter as tk
from head.head_dashboard import open_head_dashboard

from auth.login import open_login



root = tk.Tk()
root.title("School Management System")
root.geometry("500x400")

tk.Label(root, text="Pioneer School", font=("Arial", 18)).pack(pady=20)

tk.Button(root, text="Head Login", width=20, command=lambda: open_login("Head")).pack(pady=10)
tk.Button(root, text="Teacher Login", width=20, command=lambda: open_login("Teacher")).pack(pady=10)
tk.Button(root, text="Student Login", width=20, command=lambda: open_login("Student")).pack(pady=10)

root.mainloop()