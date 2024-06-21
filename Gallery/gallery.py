import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.img_files = []
        self.img_index = 0

        self.display_area = Label(root)
        self.display_area.pack()

        self.btn_prev = Button(root, text="Previous", command=self.prev_image, state=DISABLED)
        self.btn_prev.pack(side=LEFT, padx=10, pady=10)

        self.btn_next = Button(root, text="Next", command=self.next_image, state=DISABLED)
        self.btn_next.pack(side=RIGHT, padx=10, pady=10)

        self.btn_select_dir = Button(root, text="Select Directory", command=self.select_directory)
        self.btn_select_dir.pack(side=TOP, pady=20)

    def select_directory(self):
        self.img_dir = filedialog.askdirectory()
        if self.img_dir:
            self.img_files = [f for f in os.listdir(self.img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            self.img_files.sort()  # Sort the files for consistent ordering
            self.img_index = 0
            if self.img_files:
                self.show_image()
                self.btn_prev.config(state=NORMAL)
                self.btn_next.config(state=NORMAL)
            else:
                self.display_area.config(text="No images found in the selected directory.")
                self.btn_prev.config(state=DISABLED)
                self.btn_next.config(state=DISABLED)

    def show_image(self):
        img_path = os.path.join(self.img_dir, self.img_files[self.img_index])
        img = Image.open(img_path)
        img.thumbnail((700, 700))
        self.img = ImageTk.PhotoImage(img)

        self.display_area.config(image=self.img, text="")
        self.root.title(f"Image Viewer - {self.img_files[self.img_index]}")

    def next_image(self):
        self.img_index = (self.img_index + 1) % len(self.img_files)
        self.show_image()

    def prev_image(self):
        self.img_index = (self.img_index - 1) % len(self.img_files)
        self.show_image()

# Initialize the main window
root = Tk()
root.title("Image Gallery Viewer")
root.geometry("800x800")

# Create the image gallery
gallery = ImageGallery(root)

root.mainloop()
