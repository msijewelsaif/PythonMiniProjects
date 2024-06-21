import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class PDFReader:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Reader")
        self.root.geometry("800x800")

        self.pdf_document = None
        self.page_index = 0

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.btn_open = tk.Button(root, text="Open PDF", command=self.open_pdf)
        self.btn_open.pack(side=tk.TOP, pady=10)

        self.btn_prev = tk.Button(root, text="Previous Page", command=self.prev_page, state=tk.DISABLED)
        self.btn_prev.pack(side=tk.LEFT, padx=20, pady=10)

        self.btn_next = tk.Button(root, text="Next Page", command=self.next_page, state=tk.DISABLED)
        self.btn_next.pack(side=tk.RIGHT, padx=20, pady=10)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_document = fitz.open(file_path)
            self.page_index = 0
            self.show_page()
            self.btn_prev.config(state=tk.NORMAL)
            self.btn_next.config(state=tk.NORMAL)

    def show_page(self):
        if self.pdf_document:
            page = self.pdf_document[self.page_index]
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            self.img_tk = ImageTk.PhotoImage(img)

            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
            self.root.title(f"PDF Reader - Page {self.page_index + 1}")

    def next_page(self):
        if self.page_index < len(self.pdf_document) - 1:
            self.page_index += 1
            self.show_page()

    def prev_page(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.show_page()

# Initialize the main window
root = tk.Tk()
pdf_reader = PDFReader(root)
root.mainloop()
