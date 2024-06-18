from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
 
def equal():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Invalid")
    except Exception as e:
        equation_label.set("Error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("500x600")
window.configure(bg="#2fffc8")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", fg="black", width=24, height=2, relief="sunken")
label.pack(pady=20)

frame = Frame(window, bg="#b30000")
frame.pack()

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row_val = 0
col_val = 0

for button in buttons:
    action = lambda x=button: button_press(x) if x not in ["C", "="] else clear() if x == "C" else equal()
    Button(frame, text=button, height=3, width=9, font=('consolas', 14), bg="white", fg="black", command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
