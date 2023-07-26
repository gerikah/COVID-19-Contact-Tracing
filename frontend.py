import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter.font as tkfont
from PIL import Image, ImageTk
import csv

class COVID_Contacts_Information_GUI:
    def __init__(self, master):
        self.all_contacts = []
        self.new_contacrs = []
        self.master = master
        self.master.title("SAFE TRACK")
        self.master.geometry("1000x600")
        self.load_contacts_from_file()

    def load_contacts_from_file(self): # to load the contacts saved in csv
        try:
            with open("covid_contacts_record.csv", mode="r") as file:
                reader = csv.reader(file) # set read mode using csv reader
                self.all_contacts = list(reader) # save sa all_contacts
        except FileNotFoundError: # exception handling if file is not found
            pass
        except Exception as e: # error message
            raise Exception(f"Failed to load address book: {str(e)}")
        
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
    
    def show_menu(self):
        if self.menu_window is None or not self.menu_window.winfo_exists():
        # If the menu window doesn't exist or is already closed, create a new one
            self.menu_frame = tk.Frame(self.master, bg='#370607', width=1000, height=600)
            self.menu_frame.place(x=0, y=0)
            
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

            # Hide the canvas
            self.canvas.place_forget() 
            
        else:
            # If the menu window is already open, just bring it to the front
            self.menu_window.lift()
    
    # Destroy the menu window and show the main window
    def close_menu_window(self):
        self.menu_window.destroy()
        self.menu_window = None
        self.master.deiconify()

        # adding contact
    def add_contact(self, first_name, last_name, address, contact_number, date): # infos
        if any(char.isdigit() for char in first_name):
            raise Exception("First Name cannot contain numbers.")
        if any(char.isdigit() for char in last_name):
            raise Exception("Last Name cannot contain numbers.")
        if any(contact[2] == address and contact[3] == int(contact_number) for contact in self.new_contacts):
            raise Exception("The contact already exists in the address book.")
        if any(char.isalpha() for char in date):
            raise Exception("Date cannot contain letters.")
        
                # exeption handling if contact is invalid
        try:
            contact_number = int(contact_number)
            new_contact = [first_name, last_name, address, contact_number, date]
            self.new_contacts.append(new_contact)
            self.save_contacts()
        except ValueError:
            raise Exception("Contact number must be a valid number.")
        
    # save contact
    def save_contact(self):
        try:
            with open("COVID-19_contacts.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                header_row = ["First Name", "Last Name", "Address", "Contact Number", "Date"]
                writer.writerow(header_row)
                writer.writerows(self.all_contacts)
        except Exception as e:
            raise Exception(f"Failed to save address book: {str(e)}")
        
    # editing existing contact
    def edit_contact(self, contact_id, field, new_value):
        try:
            contact_id = int(contact_id)
            if 1 <= contact_id <= len(self.new_contacts):
                contact = self.new_contacts[contact_id - 1]
                if field == "First Name":
                    contact[0] = new_value
                elif field == "Last Name":
                    contact[1] = new_value
                elif field == "Address":
                    contact[2] = new_value
                elif field == "Contact Number":
                    contact[3] = new_value
                elif field == "Date":
                    contact[-1] = new_value
                self.save_contacts()
            else:
                raise Exception("Invalid contact ID.")
        except ValueError:
            raise Exception("Contact ID must be a valid number.")

    # deleting contact
    def delete_contact(self, contact_id):
        try:
            contact_id = int(contact_id)
            if 1 <= contact_id <= len(self.new_contacts):
                contact = self.new_contacts[contact_id - 1]
                self.new_contacts.remove(contact)
                self.save_contacts()
            else:
                raise Exception("Invalid contact ID.")
        except ValueError:
            raise Exception("Contact ID must be a valid number.")
 
    # for retrieving the contacts currently stored
    def get_all_contacts(self):
        return self.all_contacts + self.new_contacts      
      
    # search contact from the file
    def search_contacts (self, search_criteria, search_query):
        results = []
        for contact in self.new_contacts:
            if search_criteria == "Last Name" and search_query.lower() in contact[1].lower():
                results.append(contact)
            elif search_criteria == "First Name" and search_query.lower() in contact[0].lower():
                results.append(contact)
            elif search_criteria == "Address" and search_query.lower() in contact[2].lower():
                results.append(contact)
            elif search_criteria == "Contact Number" and search_query.lower() in str(contact[3]):
                results.append(contact)
            elif search_criteria == "Date" and search_query.lower() in contact[4].lower():
                results.append(contact)
        return results

root = tk.Tk()
gui = COVID_Contacts_Information_GUI(root)
root.mainloop()