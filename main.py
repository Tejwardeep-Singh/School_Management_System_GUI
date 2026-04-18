import tkinter as tk
from head.head_dashboard import open_head_dashboard

root = tk.Tk()
root.title("School Management System")
root.geometry("500x400")

tk.Label(root, text="Pioneer School", font=("Arial", 18)).pack(pady=20)

tk.Button(root, text="Head Login", width=20, command=open_head_dashboard).pack(pady=10)
tk.Button(root, text="Staff Login", width=20).pack(pady=10)
tk.Button(root, text="Student Login", width=20).pack(pady=10)

root.mainloop()