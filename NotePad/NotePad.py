from tkinter import *
from tkinter import filedialog

# Initialize the main window
root = Tk()
root.geometry("600x400")
root.title("Notepad")
root.config(bg="lightgray")
root.resizable(False, False)

def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if open_file is None:
        return
    text = str(text_area.get(1.0, END))
    open_file.write(text)
    open_file.close()
    print("File saved")

def open_file():
    file = filedialog.askopenfile(mode='r', filetype=[('Text files', '*.txt')])
    if file is not None:
        content = file.read()
        text_area.delete(1.0, END)
        text_area.insert(INSERT, content)
        file.close()

# Create and place the buttons and text area
btn_frame = Frame(root, bg="lightgray")
btn_frame.pack(pady=10)

save_btn = Button(btn_frame, text='Save File', command=save_file, width=20, height=2, bg='white')
save_btn.grid(row=0, column=0, padx=10)

open_btn = Button(btn_frame, text='Open File', command=open_file, width=20, height=2, bg='white')
open_btn.grid(row=0, column=1, padx=10)

text_area = Text(root, wrap=WORD, width=70, height=20)
text_area.pack(pady=10)

root.mainloop()
