import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def get_zodiac_sign(dob, tob):
    # Combining date and time to create a datetime object
    dob = datetime.strptime(dob, "%Y-%m-%d")
    tob = datetime.strptime(tob, "%H:%M")

    # Extract month and day
    month = dob.month
    day = dob.day

    # Zodiac sign determination
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return "Unknown"

def calculate_horoscope():
    try:
        dob = entry_dob.get()
        tob = entry_tob.get()
        zodiac_sign = get_zodiac_sign(dob, tob)
        messagebox.showinfo("Horoscope Checker", f"Your zodiac sign is: {zodiac_sign}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD format and time in HH:MM format")

def create_app():
    app = tk.Tk()
    app.title("Horoscope Checker")
    app.geometry("400x300")
    app.configure(bg="#ADD8E6")  # Light blue background

    title_label = tk.Label(app, text="Horoscope Checker", font=("Helvetica", 24, "bold"), bg="#ADD8E6", fg="#FFFFFF")
    title_label.pack(pady=20)

    tk.Label(app, text="Enter date of birth (YYYY-MM-DD):", bg="#ADD8E6", fg="#FFFFFF").pack(pady=5)
    global entry_dob
    entry_dob = tk.Entry(app, width=30, font=("Helvetica", 12))
    entry_dob.pack(pady=5)

    tk.Label(app, text="Enter time of birth (HH:MM):", bg="#ADD8E6", fg="#FFFFFF").pack(pady=5)
    global entry_tob
    entry_tob = tk.Entry(app, width=30, font=("Helvetica", 12))
    entry_tob.pack(pady=5)

    calculate_button = tk.Button(app, text="Check Horoscope", command=calculate_horoscope, bg="#4682B4", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
    calculate_button.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    create_app()
