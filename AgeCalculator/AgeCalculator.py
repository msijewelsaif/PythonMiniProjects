import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_date = datetime.strptime(entry.get(), "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        messagebox.showinfo("Age Calculator", f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format")

def create_app():
    app = tk.Tk()
    app.title("Age Calculator")
    app.geometry("300x300")
    tk.Label(app, text="Enter your birth date (YYYY-MM-DD):").pack(pady=10)
    global entry
    entry = tk.Entry(app)
    entry.pack(pady=5)

    tk.Button(app, text="Calculate Age", command=calculate_age).pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    create_app()
