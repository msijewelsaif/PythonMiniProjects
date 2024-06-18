import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()

def speak_text():
    text = text_entry.get("1.0", END)
    engine.say(text)
    engine.runAndWait()

root = Tk()
root.title("Text To Speech Converter")
root.geometry("400x300")
root.resizable(False, False)

obj = LabelFrame(root, text="Text To Speech", font=("Helvetica", 15), bg="#E0E0E0", fg="#333333")
obj.pack(fill="both", expand="yes", padx=10, pady=10)

text_entry = Text(obj, wrap="word", font=("Helvetica", 12), height=8, bg="#FFFFFF", fg="#000000")
text_entry.pack(padx=10, pady=10, fill="x", expand=False)

speak_button = Button(obj, text="Speak", command=speak_text, font=("Helvetica", 12), bg="#4CAF50", fg="#FFFFFF")
speak_button.pack(pady=10)

root.mainloop()
