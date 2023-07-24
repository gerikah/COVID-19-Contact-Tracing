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
        self.master.title = ("SAFE TRACK")
        self.master.geometry("1000x600")

        # Background Image
        bg_image = Image.open("background_image.jpg")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Contact Book
        self.contack_book = COVID_Contacts_Informations()
        
root = tk.Tk()
gui = COVID_Contacts_Information_GUI(root)
root.mainloop()