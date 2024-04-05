import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import function

class ImageFilterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Filtering using Fourier Transform")

        self.filter_type_var = tk.StringVar()
        self.filter_type_var.set("low-pass")

        self.cutoff_var = tk.StringVar()
        self.cutoff_var.set("50")  
        
        label = tk.Label(self, text="Choose Filter Type:")
        label.pack()

        low_pass_radio = tk.Radiobutton(self, text="Low-pass", variable=self.filter_type_var, value="low-pass")
        low_pass_radio.pack()

        high_pass_radio = tk.Radiobutton(self, text="High-pass", variable=self.filter_type_var, value="high-pass")
        high_pass_radio.pack()

        cutoff_label = tk.Label(self, text="Cutoff Frequency:")
        cutoff_label.pack()

        cutoff_entry = tk.Entry(self, textvariable=self.cutoff_var)
        cutoff_entry.pack()

        open_button = tk.Button(self, text="Open Image", command=self.open_image)
        open_button.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            filtered_image = function.apply_filter(file_path, self.filter_type_var.get(), int(self.cutoff_var.get()))
            self.show_image(filtered_image)

    def show_image(self, image):
        
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack()


if __name__ == "__main__":
    app = ImageFilterGUI()
    app.mainloop()
