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
        title_font_style = tkfont.Font(family="Poppins", size=50, weight="bold")
        welcome_label_font_style = tkfont.Font(family="Poppins", size=20, weight="bold")
        text_label_font_style = tkfont.Font(family="Poppins", size=10)

        # Title
        label_x = rect_width / 2
        label_y = rect_height / 5.5
        self.label_title = tk.Label(self.canvas, text="SAFE TRACK", font=title_font_style, bg="#370607", fg="#B0FFFA")
        self.label_title.place(x=label_x, y=label_y, anchor=tk.CENTER)

        # Tagline
        label_x = rect_width / 2
        label_y = rect_height / 3.25
        self.label_welcome = tk.Label(self.canvas, text="Stay Safe, Stay Informed: \nTrack COVID-19 with Confidence!", font=welcome_label_font_style, bg='#370607', fg="white")
        self.label_welcome.place(x=label_x, y=label_y, anchor=tk.CENTER)

        # App's purpose
        label_x = rect_width / 2
        label_y = rect_height / 1.25
        self.label_text = tk.Label(self.canvas, text="A protective tool that shields us and our loved ones \nby tracking potential COVID-19 virus exposures.", font=text_label_font_style, bg='#370607', fg="#B0FFFA")
        self.label_text.place(x=label_x, y=label_y, anchor=tk.CENTER)

        self.menu_window = None  # Store the menu window reference

        # Start button
        button_x = rect_width / 2
        button_y = (label_y + rect_height) / 3.25
        self.start_button = tk.Button(self.canvas, text="START", font=("Poppins", 30), command=self.show_menu, bg="#006B65", fg="#370607")
        self.start_button.place(x=button_x, y=button_y, anchor=tk.CENTER)

        # Contact Book
        self.contact_book = COVID_Contacts_Informations()
    
    # New window when start button has been clicked
    def show_menu(self):
        if self.menu_window is None or not self.menu_window.winfo_exists():
        # If the menu window doesn't exist or is already closed, create a new one
            self.menu_window = tk.Toplevel(self.master)
            self.menu_window.title("SAFE TRACK")
            self.menu_window.geometry("1000x600")

            # Background Image
            bg_image = Image.open("background_image.jpg")
            bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(self.master, image=bg_photo)
            bg_label.image = bg_photo
            bg_label.place(x=0, y=2, relwidth=1, relheight=1)
            
            # Add Contact Button
            add_button = tk.Button(self.menu_window, text="Add Contact", font=("Poppins", 16), command=self.add_contact)
            add_button.pack(pady=10)

            # Edit Contact Button
            edit_button = tk.Button(self.menu_window, text="Edit Contact", font=("Poppins", 16), command=self.edit_contact)
            edit_button.pack(pady=10)

            # Delete Contact Button
            delete_button = tk.Button(self.menu_window, text="Delete Contact", font=("Poppins", 16), command=self.delete_contact)
            delete_button.pack(pady=10)

            # View Contacts Button
            view_button = tk.Button(self.menu_window, text="View Contacts", font=("Poppins", 16), command=self.view_contacts)
            view_button.pack(pady=10)

            # Search Contact Book Button
            search_button = tk.Button(self.menu_window, text="Search Contact Book", font=("Poppins", 16), command=self.search_contact)
            search_button.pack(pady=10)

            # Exit Button
            exit_button = tk.Button(self.menu_window, text="Exit", font=("Poppins", 16), command=self.close_menu_window)
            exit_button.pack(pady=10)
            
            # Set the function to be called when the menu window is closed
            self.menu_window.protocol("WM_DELETE_WINDOW", self.close_menu_window)

            # Hide the main window
            self.master.withdraw()
            
        else:
            # If the menu window is already open, just bring it to the front
            self.menu_window.lift()
    
    # Destroy the menu window and show the main window
    def close_menu_window(self):
        self.menu_window.destroy()
        self.menu_window = None
        self.master.deiconify()

root = tk.Tk()
gui = COVID_Contacts_Information_GUI(root)
root.mainloop()