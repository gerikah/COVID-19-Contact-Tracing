import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkfont
from PIL import Image, ImageTk
from backend import COVID_Contacts_Informations

class COVID_Contacts_Information_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("SAFE TRACK")
        self.master.geometry("1000x600")

        # Background Image
        bg_image = Image.open("background_image.jpg")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.master, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=2, relwidth=1, relheight=1)

        # Canvas widget for rectangle
        self.canvas = tk.Canvas(self.master, bg='#370607', width=700, height=600)
        self.canvas.place(x=0, y=0)
        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()
        rect_width = canvas_width
        rect_height = canvas_height
        self.canvas.create_rectangle(0, 0, rect_width, rect_height, fill='#370607')
        
        # Font Style
        font_style = tkfont.Font(family="Poppins", size=50, weight="bold")

        # Title
        label_x = rect_width / 2
        label_y = rect_height / 5.5
        self.label_title = tk.Label(self.canvas, text="SAFE TRACK", font=font_style, bg='#370607', fg="white")
        self.label_title.place(x=label_x, y=label_y, anchor=tk.CENTER)

        # Tagline
        label_x = rect_width / 2
        label_y = rect_height / 3.25
        self.label_welcome = tk.Label(self.canvas, text="Stay Safe, Stay Informed: \nTrack COVID-19 with Confidence!", font=("Poppins", 20), bg='#370607', fg="#B0FFFA")
        self.label_welcome.place(x=label_x, y=label_y, anchor=tk.CENTER)

        # App's purpose
        label_x = rect_width / 2
        label_y = rect_height / 1.25
        self.label_welcome = tk.Label(self.canvas, text="A protective tool that shields us and our loved ones \nby tracking potential COVID-19 virus exposures.", font=("Poppins", 10), bg='#370607', fg="white")
        self.label_welcome.place(x=label_x, y=label_y, anchor=tk.CENTER)

        self.menu_window = None  # Store the menu window reference

        self.start_button = tk.Button(self.master, text="Start", command=self.show_menu)
        self.start_button.pack(pady=50)

        # Contact Book
        self.contact_book = COVID_Contacts_Informations()
        
    def show_menu(self):
        pass

root = tk.Tk()
gui = COVID_Contacts_Information_GUI(root)
root.mainloop()