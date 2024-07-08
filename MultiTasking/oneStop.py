import tkinter as tk
from tkinter import messagebox
import requests

class AddressBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book with Extras")
        self.root.geometry("600x400")

        # Address Book Data
        self.contacts = []
        self.current_contact = None

        # Clock
        self.clock_label = tk.Label(self.root, font=("Arial", 14))
        self.clock_label.pack(pady=10)

        # Weather Information
        self.weather_label = tk.Label(self.root, font=("Arial", 14))
        self.weather_label.pack(pady=10)

        # Text Editor
        self.text_editor = tk.Text(self.root, font=("Arial", 12), height=10, wrap=tk.WORD)
        self.text_editor.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        save_button = tk.Button(button_frame, text="Save Note", font=("Arial", 12), command=self.save_note)
        save_button.grid(row=0, column=0, padx=5)

        load_button = tk.Button(button_frame, text="Load Note", font=("Arial", 12), command=self.load_note)
        load_button.grid(row=0, column=1, padx=5)

        fetch_weather_button = tk.Button(button_frame, text="Fetch Weather", font=("Arial", 12), command=self.fetch_weather)
        fetch_weather_button.grid(row=0, column=2, padx=5)

        self.update_clock()
        self.fetch_weather()

    def update_clock(self):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.clock_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_clock)

    def fetch_weather(self):
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        city = 'New York'  # Replace with user's location or input field
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

        try:
            response = requests.get(url)
            data = response.json()
            weather_info = f"Weather in {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
            self.weather_label.config(text=weather_info)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch weather: {e}")

    def save_note(self):
        note_content = self.text_editor.get("1.0", tk.END)
        if self.current_contact:
            self.current_contact["note"] = note_content
            messagebox.showinfo("Saved", "Note saved successfully.")
        else:
            messagebox.showwarning("Warning", "No contact selected.")

    def load_note(self):
        if self.current_contact and "note" in self.current_contact:
            self.text_editor.delete("1.0", tk.END)
            self.text_editor.insert(tk.END, self.current_contact["note"])
        else:
            messagebox.showwarning("Warning", "No note available for the selected contact.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()
