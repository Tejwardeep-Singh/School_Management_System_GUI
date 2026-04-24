import tkinter as tk
from auth.login import open_login

BG_COLOR = "#0f172a"
BTN_COLOR = "#3b82f6"
TEXT_COLOR = "#f1f5f9"

root = tk.Tk()
root.title("School Management System")
root.geometry("500x400")
root.configure(bg=BG_COLOR)

tk.Label(root, text="Pioneer School",
         font=("Segoe UI", 20, "bold"),
         fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=30)

def styled_button(text, role):
    return tk.Button(
        root,
        text=text,
        command=lambda: open_login(role),
        width=20,
        height=2,
        bg=BTN_COLOR,
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2"
    )

styled_button("Head Login", "Head").pack(pady=10)
styled_button("Teacher Login", "Teacher").pack(pady=10)
styled_button("Student Login", "Student").pack(pady=10)

root.mainloop()