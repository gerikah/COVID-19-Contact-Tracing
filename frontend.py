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

        # Font Style
        font_style = tkfont.Font(family="Poppins", size=30, weight="bold")
        self.label_title = tk.Label(self.master, text="SAFE TRACK", font=font_style, bg="#006B65")
        self.label_title.pack(pady=30, anchor=tk.CENTER)

        # for tagline
        self.label_welcome = tk.Label(
            self.master, text="Stay Safe, Stay Informed: Track COVID-19 with Confidence!", font=("Poppins", 10), bg="#006B65")
        self.label_welcome.pack()

        self.menu_window = None  # Store the menu window reference

        self.start_button = tk.Button(self.master, text="Start", command=self.show_menu)
        self.start_button.pack(pady=20)

        # Contact Book
        self.contact_book = COVID_Contacts_Informations()
        
    def show_menu(self):
        pass

root = tk.Tk()
gui = COVID_Contacts_Information_GUI(root)
root.mainloop()