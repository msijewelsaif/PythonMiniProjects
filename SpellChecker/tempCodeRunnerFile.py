from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("500x500")
root.config(background="#dae6f6")
root.resizable(False,False)

heading =Label(root,text="Spelling Check",font=("Trebuchet MS",20,"Bold"),bg="white",fg="#3")
root.mainloop()