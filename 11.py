import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.label = tk.Label(root, text="Введите текст:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button_load = tk.Button(root, text="Загрузить изображение", command=self.load_image)
        self.button_load.pack()

        self.button_process = tk.Button(root, text="Объединить", command=self.process_image)
        self.button_process.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.show_image()

    def show_image(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.config(width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def process_image(self):
        if hasattr(self, 'image'):
            text = self.entry.get()
            if text:
                draw = ImageDraw.Draw(self.image)
                font = ImageFont.load_default()
                text_bbox = draw.textbbox((0, 0), text, font=font)
                x = (self.image.width - text_bbox[2]) // 2
                y = self.image.height - text_bbox[3] - 10
                draw.text((x, y), text, font=font, fill=(255, 255, 255))
                self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root)
    root.mainloop()
