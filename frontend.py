import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import filedialog
from tkinter import ttk
import re
import tkinter.font as tkfont
from PIL import Image, ImageTk
import csv

class COVID_Contacts_Information:
    def __init__(self, master):
        self.all_contacts = []
        self.new_contacts = []
        self.master = master
        self.master.title("SAFE TRACK")
        self.master.geometry("1000x600")
        self.load_contacts_from_file()
        self.menu_frame = tk.Frame(self.master, bg='#370607', width=1000, height=600)
        self.create_menu_content()
        
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
    
    def load_contacts_from_file(self): # to load the contacts saved in csv
        try:
            with open("covid_contacts_record.csv", mode="r") as file:
                reader = csv.reader(file) # set read mode using csv reader
                self.all_contacts = list(reader) # save sa all_contacts
        except FileNotFoundError: # exception handling if file is not found
            pass
        except Exception as e: # error message
            raise Exception(f"Failed to load address book: {str(e)}")
    
    def save_contacts(self):
        try:
            with open("address_book.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(self.all_contacts + self.new_contacts)  # Save all contacts together
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save address book: {str(e)}")

    def show_menu(self):
        if self.menu_window is None or not self.menu_window.winfo_exists():
        # If the menu window doesn't exist or is already closed, create a new one
            self.menu_window = tk.Toplevel(self.master)
            self.menu_window.title("Menu")
            self.menu_window.geometry("1000x600")
            self.menu_frame = tk.Frame(self.menu_window, bg='#370607', width=1000, height=600)
            self.menu_frame.place(x=0, y=0)

            # Set the function to be called when the menu window is closed
            self.menu_window.protocol("WM_DELETE_WINDOW", self.close_menu_window)

            # Content for menu window
            self.create_menu_content()
            
            # Hide the canvas
            self.canvas.place_forget() 
            
        else:
            # If the menu window is already open, just bring it to the front
            self.menu_window.lift()

    def create_menu_content(self):
        self.file_button = tk.Button(self.menu_frame, width=20, text="Select File", background='white',font=("Times New Roman", 12, "bold"), command=self.load_contacts_from_file)
        self.file_button.pack(pady=10, padx=750)
        self.add_button = tk.Button(self.menu_frame, width=20, text="Add Contact", background='white', font=("Times New Roman", 12, "bold"), command=self.add_contact)
        self.add_button.pack(pady=15, padx=750)
        self.edit_button = tk.Button(self.menu_frame, width=20, text="Edit Contact", background='white', font=("Times New Roman", 12, "bold"), command=self.edit_contact)
        self.edit_button.pack(pady=10, padx=750)
        self.delete_button = tk.Button(self.menu_frame, width=20, text="Delete Contact", background='white', font=("Times New Roman", 12, "bold"), command=self.delete_contact)
        self.delete_button.pack(pady=15, padx=750)
        self.view_button = tk.Button(self.menu_frame, width=20, text="View Contacts", background='white', font=("Times New Roman", 12, "bold"), command=self.view_contacts)
        self.view_button.pack(pady=10, padx=750)
        self.search_button = tk.Button(self.menu_frame, width=20, text="Search Address Book", background='white', font=("Times New Roman", 12, "bold"), command=self.search_address_book)
        self.search_button.pack(pady=15, padx=750)
        self.exit_button = tk.Button(self.menu_frame, width=10, text="Exit", background='white', font=("Times New Roman", 12, "bold"), command=self.on_exit)
        self.exit_button.pack(pady=10, padx=750)

    # The functions for the new buttons
    def button1_function(self):
        messagebox.showinfo("Button 1 Clicked", "Button 1 was clicked!")

    def button2_function(self):
        messagebox.showinfo("Button 2 Clicked", "Button 2 was clicked!")
        
    def add_existing_file(self):
        file_path = filedialog.askopenfilename(title="Select Existing File", filetypes=[("CSV Files", "*.csv"),("TXT Files", "*.txt"),("PDF Files","*.pdf")])
        if file_path:
            try:
                with open(file_path, mode="r") as file:
                    reader = csv.reader(file)
                    contacts = list(reader)
                    self.new_contacts.extend(contacts)  # Add contacts to the new contacts list
                    self.save_contacts()  # Save all contacts
                    messagebox.showinfo("Success", "File added successfully.")
            except FileNotFoundError:
                messagebox.showerror("File Not Found", "The selected file does not exist.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add file: {str(e)}")

    def add_contact(self):
        window = tk.Toplevel(self.master)
        window.title("Add Contact")
        window.geometry("300x200")
        window.resizable(False, False)

        # Entry fields
        first_name_label = tk.Label(window, text="First Name:")
        first_name_entry = tk.Entry(window)
        first_name_label.pack()
        first_name_entry.pack()

        last_name_label = tk.Label(window, text="Last Name:")
        last_name_entry = tk.Entry(window)
        last_name_label.pack()
        last_name_entry.pack()

        address_label = tk.Label(window, text="Email Address:")
        address_entry = tk.Entry(window)
        address_label.pack()
        address_entry.pack()

        contact_number_label = tk.Label(window, text="Contact Number:")
        contact_number_entry = tk.Entry(window)
        contact_number_label.pack()
        contact_number_entry.pack()

        def save_contact():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            address = address_entry.get()
            contact_number = contact_number_entry.get()

            if first_name and last_name and address and contact_number:
                if any(char.isdigit() for char in first_name):
                    messagebox.showinfo("Invalid Input", "First Name cannot contain numbers.")
                elif any(char.isdigit() for char in last_name):
                    messagebox.showinfo("Invalid Input", "Last Name cannot contain numbers.")
                elif not re.match(r"[^@]+@[^@]+\.[^@]+", address) or "@gmail.com" not in address:
                    messagebox.showinfo("Invalid Input", "Invalid or email address.")
                elif any(contact[2] == address and contact[3] == int(contact_number) for contact in self.new_contacts):
                    messagebox.showinfo("Duplicate Entry", "The contact already exists in the address book.")
                else:
                    try:
                        contact_number = int(contact_number)  # Convert the contact number to an integer
                        new_contact = [first_name, last_name, address, contact_number]
                        self.new_contacts.append(new_contact)  # Add the contact to the new contacts list
                        messagebox.showinfo("Success", "Contact added successfully.")
                        window.destroy()
                    except ValueError:
                        messagebox.showinfo("Invalid Input", "Contact number must be a valid number.")
            else:
                messagebox.showinfo("Invalid Input", "All fields are required.")

        save_button = tk.Button(window, text="Save", command=save_contact)
        save_button.pack()
            
    def edit_contact(self):
        contact_id = simpledialog.askstring("Edit Contact", "Enter Contact ID:")
        if contact_id:
            try:
                contact_id = int(contact_id)  # Convert the contact ID to an integer
                if 1 <= contact_id <= len(self.new_contacts):
                    contact = self.new_contacts[contact_id - 1]  # Get the contact based on the ID
                    edit_options = ["First Name", "Last Name", "Email Address", "Contact Number"]
                    selected_option = tk.StringVar()
                    selected_option.set("Edit by:")

                    # Create the edit contact window
                    edit_window = tk.Toplevel(self.master)
                    edit_window.title("Edit Contact")
                    edit_window.geometry("300x200")
                    edit_window.resizable(False, False)

                    # Entry fields
                    edit_label = tk.Label(edit_window, text="Select field to edit:")
                    edit_label.pack()

                    dropdown = tk.OptionMenu(edit_window, selected_option, *edit_options)
                    dropdown.pack(pady=10)

                    new_value_label = tk.Label(edit_window, text="Enter new value:")
                    new_value_label.pack()

                    new_value_entry = tk.Entry(edit_window)
                    new_value_entry.pack()

                    def save_edit():
                        new_value = new_value_entry.get()
                        if new_value:
                            selected_option_value = selected_option.get()

                            # Validate new value for First Name or Last Name
                            if selected_option_value in ["First Name", "Last Name"]:
                                if not new_value.isalpha():
                                    messagebox.showinfo("Invalid Input", "Please enter alphabetical letters only.")
                                    return

                            if selected_option_value == "Contact Number":
                                # Allow spaces and "+" sign in the contact number
                                new_value = new_value.replace(" ", "").replace("+", "")

                            # Check if the new value already exists in the address book
                            if selected_option_value == "Email Address":
                                duplicate = any(
                                    contact[2] == new_value and contact[3] == contact[-1] for contact in self.new_contacts
                                )
                            elif selected_option_value == "Contact Number":
                                duplicate = any(
                                    contact[2] == contact[2] and contact[3] == str(new_value) for contact in self.new_contacts
                                )
                            else:
                                duplicate = False

                            if duplicate:
                                messagebox.showinfo(
                                    "Duplicate Entry", "The contact with the new information already exists in the address book."
                                )
                            else:
                                contact[edit_options.index(selected_option_value)] = new_value
                                messagebox.showinfo("Success", "Contact updated successfully.")
                                edit_window.destroy()
                                self.save_contacts()  # Save the updated contacts
                                self.view_contacts()  # Refresh the view contacts window
                        else:
                            messagebox.showinfo("Invalid Input", "New value is required.")


                    save_button = tk.Button(edit_window, text="Save", command=save_edit)
                    save_button.pack()

                else:
                    messagebox.showinfo("Invalid Input", "Invalid contact ID.")
            except ValueError:
                messagebox.showinfo("Invalid Input", "Contact ID must be a valid number.")
        else:
            messagebox.showinfo("Invalid Input", "Contact ID is required.")
            
    def update_contact(self, option, contact):
        if option == "First Name":
            new_value = simpledialog.askstring("Edit Contact", "Enter new First Name:")
            if new_value:
                contact[0] = new_value
                messagebox.showinfo("Success", "Contact updated successfully.")
        elif option == "Last Name":
            new_value = simpledialog.askstring("Edit Contact", "Enter new Last Name:")
            if new_value:
                contact[1] = new_value
                messagebox.showinfo("Success", "Contact updated successfully.")
        elif option == "Address":
            new_value = simpledialog.askstring("Edit Contact", "Enter new Address:")
            if new_value:
                contact[2] = new_value
                messagebox.showinfo("Success", "Contact updated successfully.")
        elif option == "Contact Number":
            new_value = simpledialog.askstring("Edit Contact", "Enter new Contact Number:")
            if new_value:
                contact[3] = new_value
                messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showinfo("Invalid Input", "Please select a valid option.")

    def delete_contact(self):
        contact_id = simpledialog.askstring("Delete Contact", "Enter Contact ID:")
        if contact_id:
            try:
                contact_id = int(contact_id)  # Convert the contact ID to an integer
                if 1 <= contact_id <= len(self.new_contacts):
                    contact = self.new_contacts[contact_id - 1]  # Get the contact based on the ID
                    self.new_contacts.remove(contact)  # Remove the contact from the new contacts list
                    messagebox.showinfo("Success", "Contact deleted successfully.")

                    # Update and save the contacts to the CSV file
                    with open("address_book.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(self.new_contacts)

                else:
                    messagebox.showinfo("Invalid Input", "Invalid contact ID.")
            except ValueError:
                messagebox.showinfo("Invalid Input", "Contact ID must be a valid number.")
        else:
            messagebox.showinfo("Invalid Input", "Contact ID is required.")

    def view_contacts(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Contacts")
        view_window.geometry("600x400")
        view_window.resizable(True, True)

        tree = ttk.Treeview(view_window)
        tree["columns"] = ("First Name", "Last Name", "Email Address", "Contact Number")
        tree.heading("#0", text="ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Email Address", text="Email Address")
        tree.heading("Contact Number", text="Contact Number")

        # Configure column widths
        tree.column("#0", width= 50)
        tree.column("First Name", width=80)
        tree.column("Last Name", width=80)
        tree.column("Email Address", width=200)
        tree.column("Contact Number", width=100)

        # Insert data into the treeview
        for i, contact in enumerate(self.new_contacts):
            tree.insert("", tk.END, text=str(i + 1), values=(contact[0], contact[1], contact[2], contact[3]))

        tree.pack()
        
    def search_address_book(self):
        search_window = tk.Toplevel(self.master)
        search_window.title("Search Address Book")
        search_window.geometry("400x200")
        search_window.resizable(False, False)

        label = tk.Label(search_window, text="Select search criteria:")
        label.pack(pady=10)

        search_options = ["Last Name", "First Name", "Address", "Contact Number"]
        selected_option = tk.StringVar()
        selected_option.set("Search by:")
        dropdown = tk.OptionMenu(search_window, selected_option, *search_options)
        dropdown.pack()

        entry_label = tk.Label(search_window, text="Enter search query:")
        entry_label.pack(pady=10)

        entry = tk.Entry(search_window)
        entry.pack()

        search_button = tk.Button(search_window, text="Search", command=lambda: self.perform_search(selected_option.get(), entry.get()))
        search_button.pack(pady=10)
        
        search_window.mainloop()

    def perform_search(self, search_criteria, search_query):
        if search_query:
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

            if results:
                search_results_window = tk.Toplevel(self.master)
                search_results_window.title("Search Results")
                search_results_window.geometry("600x200")
                search_results_window.resizable(False, False)

                tree = ttk.Treeview(search_results_window)
                tree["columns"] = ("First Name", "Last Name", "Address", "Contact Number")
                tree.heading("#0", text="ID")
                tree.heading("First Name", text="First Name")
                tree.heading("Last Name", text="Last Name")
                tree.heading("Address", text="Address")
                tree.heading("Contact Number", text="Contact Number")

                # Configure column widths
                tree.column("#0", width=50)
                tree.column("First Name", width=100)
                tree.column("Last Name", width=100)
                tree.column("Address", width=200)
                tree.column("Contact Number", width=100)

                # Insert data into the treeview
                for i, contact in enumerate(results):
                    tree.insert("", tk.END, text=str(i + 1), values=(contact[0], contact[1], contact[2], contact[3]))

                tree.pack()
            else:
                messagebox.showinfo("No Results", "No contacts match the search query.")
        else:
            messagebox.showinfo("Invalid Input", "Search query is required.")
    
    def on_exit(self):
        # Close the entire application by destroying the root window
        self.master.destroy()

    # Destroy the menu window and show the main window
    def close_menu_window(self):
        self.menu_frame.place_forget()
        self.canvas.place(x=0, y=0)

root = tk.Tk()
gui = COVID_Contacts_Information(root)
root.mainloop()