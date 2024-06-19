from tkinter import *
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("500x400")
root.config(background="#e6e6fa")
root.resizable(False, False)

def check_spelling():
    word = enter_text.get()
    if not word:
        messagebox.showwarning("Input Error", "Please insert a word")
        return
    blob = TextBlob(word)
    corrected_word = str(blob.correct())
    if word == corrected_word:
        spell.config(text=f"Spelling is correct: {corrected_word}", fg="green")
    else:
        spell.config(text=f"Incorrect spelling: {word}\nCorrect spelling: {corrected_word}", fg="red")

def clear_text():
    enter_text.delete(0, END)
    spell.config(text="")

heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 24, "bold"), bg="#e6e6fa", fg="#4b0082")
heading.pack(pady=(30, 10))

enter_text = Entry(root, justify="center", width=30, font=("Arial", 18), bg="#dcdcdc", fg="black", border=2)
enter_text.pack(pady=(10, 20))
enter_text.focus()

button_frame = Frame(root, bg="#e6e6fa")
button_frame.pack(pady=(10, 20))

check_button = Button(button_frame, text="Check", font=("Arial", 18, "bold"), bg="#4b0082", fg="white", command=check_spelling)
check_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear", font=("Arial", 18, "bold"), bg="#4b0082", fg="white", command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

spell = Label(root, font=("Arial", 18), bg="#e6e6fa", fg="crimson")
spell.pack(pady=(10, 20))

root.mainloop()
