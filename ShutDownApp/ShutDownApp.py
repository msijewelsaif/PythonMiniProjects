from tkinter import *
import os

root = Tk()
root.title("Shutdown App")
root.geometry("400x400")

root.resizable(False, False)

def restart():
    os.system("shutdown /r /t 30")

def shutDown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown -l")

restart_button = Button(root, text="Restart", font=("Arial", 20, "bold"), cursor="hand2", command=restart)
restart_button.place(x=100, y=10)

shutDown_button = Button(root, text="Shut Down", font=("Arial", 20, "bold"), cursor="hand2", command=shutDown)
shutDown_button.place(x=100, y=100)

logout_button = Button(root, text="Log Out", font=("Arial", 20, "bold"), cursor="hand2", command=logout)
logout_button.place(x=100, y=200)

root.mainloop()
