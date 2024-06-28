import tkinter as tk
from datetime import datetime, timedelta
import time

class ClockTimerStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock, Timer, Stopwatch")
        self.root.geometry("400x400")
        self.root.configure(bg="#ADD8E6")  # Light blue background
        
        self.clock_label = tk.Label(root, font=("Helvetica", 24), bg="#ADD8E6", fg="#FFFFFF")
        self.clock_label.pack(pady=20)
        self.update_clock()

        # Timer
        self.timer_running = False
        self.timer_time = 0
        self.timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24), bg="#ADD8E6", fg="#FFFFFF")
        self.timer_label.pack(pady=10)
        self.timer_entry = tk.Entry(root, font=("Helvetica", 12))
        self.timer_entry.pack(pady=5)
        self.timer_entry.insert(0, "Enter time in seconds")
        self.start_timer_button = tk.Button(root, text="Start Timer", command=self.start_timer, bg="#4682B4", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
        self.start_timer_button.pack(pady=5)

        # Stopwatch
        self.stopwatch_running = False
        self.stopwatch_time = 0
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24), bg="#ADD8E6", fg="#FFFFFF")
        self.stopwatch_label.pack(pady=10)
        self.start_stopwatch_button = tk.Button(root, text="Start Stopwatch", command=self.start_stopwatch, bg="#4682B4", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
        self.start_stopwatch_button.pack(pady=5)
        self.stop_stopwatch_button = tk.Button(root, text="Stop Stopwatch", command=self.stop_stopwatch, bg="#4682B4", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
        self.stop_stopwatch_button.pack(pady=5)
        self.reset_stopwatch_button = tk.Button(root, text="Reset Stopwatch", command=self.reset_stopwatch, bg="#4682B4", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
        self.reset_stopwatch_button.pack(pady=5)

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def start_timer(self):
        if not self.timer_running:
            try:
                self.timer_time = int(self.timer_entry.get())
                self.timer_running = True
                self.update_timer()
            except ValueError:
                tk.messagebox.showerror("Invalid Input", "Please enter a valid time in seconds")

    def update_timer(self):
        if self.timer_running:
            if self.timer_time > 0:
                self.timer_time -= 1
                time_str = str(timedelta(seconds=self.timer_time))
                self.timer_label.config(text=time_str)
                self.root.after(1000, self.update_timer)
            else:
                self.timer_running = False
                tk.messagebox.showinfo("Timer", "Time's up!")

    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.update_stopwatch()

    def stop_stopwatch(self):
        self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_time = 0
        self.stopwatch_label.config(text="00:00:00")

    def update_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_time += 1
            time_str = str(timedelta(seconds=self.stopwatch_time))
            self.stopwatch_label.config(text=time_str)
            self.root.after(1000, self.update_stopwatch)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockTimerStopwatchApp(root)
    root.mainloop()
