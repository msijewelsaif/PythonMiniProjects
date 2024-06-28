import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

def calculate_love_score():
    try:
        dob1 = datetime.strptime(entry1.get(), "%Y-%m-%d")
        dob2 = datetime.strptime(entry2.get(), "%Y-%m-%d")
        random.seed(dob1.toordinal() + dob2.toordinal())
        love_score = random.randint(50, 100)  # Generate a random love score between 50 and 100
        messagebox.showinfo("Love Calculator", f"Your love score is: {love_score}%")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter valid dates in YYYY-MM-DD format")

def create_app():
    app = tk.Tk()
    app.title("Love Calculator")
    app.geometry("400x300")
    app.configure(bg="#FFC0CB")  # Light pink background

    title_label = tk.Label(app, text="Love Calculator", font=("Helvetica", 24, "bold"), bg="#FFC0CB", fg="#FFFFFF")
    title_label.pack(pady=20)

    tk.Label(app, text="Enter first date of birth (YYYY-MM-DD):", bg="#FFC0CB", fg="#FFFFFF").pack(pady=5)
    global entry1
    entry1 = tk.Entry(app, width=30, font=("Helvetica", 12))
    entry1.pack(pady=5)

    tk.Label(app, text="Enter second date of birth (YYYY-MM-DD):", bg="#FFC0CB", fg="#FFFFFF").pack(pady=5)
    global entry2
    entry2 = tk.Entry(app, width=30, font=("Helvetica", 12))
    entry2.pack(pady=5)

    calculate_button = tk.Button(app, text="Calculate Love Score", command=calculate_love_score, bg="#FF69B4", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
    calculate_button.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    create_app()
