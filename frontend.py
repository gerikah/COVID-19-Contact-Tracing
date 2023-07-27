import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import filedialog
from tkinter import ttk
import re
import tkinter.font as tkfont
from PIL import Image, ImageTk
import csv
import copy


class COVID_Contacts_Information:
    def __init__(self, master):
        self.all_contacts = []
        self.new_contacts = []
        self.master = master
        self.master.title("SAFE TRACK")
        self.master.geometry("1000x600")
        self.master.configure(bg="#370607")
        self.load_contacts_from_file()
        self.menu_window = None

        # Background Image
        bg_image = Image.open("C:\\Users\\gerik\\OneDrive\\Documents\\GitHub\\COVID-19-Contact-Tracing\\Main Window Image - Virus.jpg")
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

        # Start button
        button_x = rect_width / 2
        button_y = (label_y + rect_height) / 3.25
        self.start_button = tk.Button(self.canvas, text="START", font=("Poppins", 30), command=self.on_start_button_click, bg="#006B65", fg="#370607")
        self.start_button.place(x=button_x, y=button_y, anchor=tk.CENTER)

    def load_contacts_from_file(self):
        try:
            with open("covid_contacts_record.csv", mode="r") as file:
                reader = csv.reader(file)
                header = next(reader)  # Skip the header row
                self.all_contacts = list(reader)

                # Check if the file is empty
                if not self.all_contacts:
                    # Optionally, you can choose to display a message to the user
                    messagebox.showinfo("Empty Contact Book", "The contact book is empty.")
                    return  # Return without raising an exception or copying the contacts

                # Convert the symptoms back to a dictionary
                for contact in self.all_contacts:
                    if len(contact) == 8:  # Check the length of the contact before unpacking
                        symptoms_str = contact[4]
                        symptoms_dict = {symptom: True if symptom in symptoms_str else False for symptom in ["Cough", "Fever", "Breathing Difficulties"]}
                        contact[4] = symptoms_dict
                    else:
                        raise Exception("Invalid format in the contact book.")

                # Clear the existing entries in new_contacts before loading contacts from the file
        except FileNotFoundError:
            self.all_contacts = []  # Initialize as an empty list if the file is not found
            self.save_contacts()
        except Exception as e:
            raise Exception(f"Failed to load contact book: {str(e)}")

        # Use deepcopy to ensure that we are not modifying the original data
        self.new_contacts = copy.deepcopy(self.all_contacts)
        
    def save_contacts(self):
        try:
            with open("covid_contacts_record.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Email Address", "Contact Number", "Symptoms", "First Vaccine", "Second Vaccine", "Booster Shot"])
                writer.writerows(self.all_contacts + self.new_contacts)  # Save all contacts together
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save address book: {str(e)}")
    
    def save_symptoms(self, symptoms):
        symptoms_str = ", ".join(symptom for symptom, status in symptoms.items() if status)
        return symptoms_str

    def save_vaccination_status(self, vaccines):
        return "Yes" if vaccines else "No"
    
    def on_start_button_click(self):
        # Destroy the main window
        self.master.withdraw()
        self.show_menu()

    def create_menu_content(self):
        self.add_button = tk.Button(self.menu_window, width=20, text="Add Contact", background='#370607', fg="white", bd=5, font=("Poppins", 12, "bold"), command=self.add_contact)
        self.add_button.place(x=900, y=80, anchor=tk.NE)
        self.edit_button = tk.Button(self.menu_window, width=20, text="Edit Contact", background='#370607', fg="white", bd=5, font=("Poppins", 12, "bold"), command=self.edit_contact)
        self.edit_button.place(x=900, y=160, anchor=tk.NE)
        self.delete_button = tk.Button(self.menu_window, width=20, text="Delete Contact", background='#370607', fg="white", bd=5, font=("Poppins", 12, "bold"), command=self.delete_contact)
        self.delete_button.place(x=900, y=240, anchor=tk.NE)
        self.view_button = tk.Button(self.menu_window, width=20, text="View Contacts", background='#370607', fg="white", bd=5, font=("Poppins", 12, "bold"), command=self.view_contacts)
        self.view_button.place(x=900, y=320, anchor=tk.NE)
        self.search_button = tk.Button(self.menu_window, width=20, text="Search Contact", background='#370607', fg="white", bd=5, font=("Poppins", 12, "bold"), command=self.search_contacts)
        self.search_button.place(x=900, y=400, anchor=tk.NE)
        self.exit_button = tk.Button(self.menu_window, width=10, text="Exit", background='#370607', fg="white", bd=5, font=("Poppins", 12, "bold"), command=self.on_exit)
        self.exit_button.place(x=855, y=480, anchor=tk.NE)

    def show_menu(self):
        if self.menu_window is None or not self.menu_window.winfo_exists():
            # If the menu window doesn't exist or is already closed, create a new one
            self.menu_window = tk.Toplevel(self.master)
            self.menu_window.title("Menu")
            self.menu_window.geometry("1000x600")
            self.menu_window.protocol("WM_DELETE_WINDOW", self.close_menu_window)
            self.canvas = tk.Canvas(self.menu_window, width=1000, height=600)
            self.canvas.pack()

            # Add a rectangle on the left side of the canvas
            self.canvas.create_rectangle(0, 0, 600, 600, fill="#A6A6A6")

            # Load the image
            bg_image = Image.open("C:\\Users\\gerik\\OneDrive\\Documents\\GitHub\\COVID-19-Contact-Tracing\\Menu Window Image - Safe Trace.png")
            bg_image = bg_image.resize((500, 600))
            bg_photo = ImageTk.PhotoImage(bg_image)

            # Create a label with the image
            bg_label = tk.Label(self.canvas, image=bg_photo)
            bg_label.image = bg_photo

            # Place the label inside the canvas
            self.canvas.create_window(250, 300, window=bg_label)
            self.create_menu_content()  # Content for menu window

        else:
            # If the menu window is already open, just bring it to the front
            self.menu_window.lift()

        self.menu_window.deiconify()

    def add_contact(self):
        new_contact_added = False

        def save_contact():
            nonlocal new_contact_added
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            address = address_entry.get()
            contact_number = contact_number_entry.get()
            symptoms = {
                "Cough": self.cough_var.get(),
                "Fever": self.fever_var.get(),
                "Breathing Difficulties": self.breathing_var.get()}
            first_vaccine = self.first_vaccine_var.get()
            second_vaccine = self.second_vaccine_var.get()
            booster_shot = self.booster_shot_var.get()
        
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
                        new_contact = [first_name, last_name, address, contact_number, symptoms, first_vaccine, second_vaccine, booster_shot]
                        self.new_contacts.append(new_contact)  # Add the contact to the new contacts list
                        self.save_contacts()
                        new_contact_added = True
                        # Clear the entry fields after saving the contact
                        first_name_entry.delete(0, tk.END)
                        last_name_entry.delete(0, tk.END)
                        address_entry.delete(0, tk.END)
                        contact_number_entry.delete(0, tk.END)

                        # Clear the symptom checkboxes
                        self.cough_var.set(False)
                        self.fever_var.set(False)
                        self.breathing_var.set(False)

                        # Clear the vaccination checkboxes
                        self.first_vaccine_var.set(False)
                        self.second_vaccine_var.set(False)
                        self.booster_shot_var.set(False)
                        messagebox.showinfo("Success", "Contact added successfully.")
                        window.destroy()
                        self.show_menu()
                        self.menu_window.deiconify()
                    except ValueError:
                        messagebox.showinfo("Invalid Input", "Contact number must be a valid number.")
            else:
                messagebox.showinfo("Invalid Input", "All fields are required.")

        window = tk.Toplevel(self.menu_window)
        window.title("Add Contact")
        window.geometry("1000x600")
        window.resizable(False, False)

        # Entry fields
        label_font_style = tkfont.Font(family="Poppins", size=12)
        entry_width = 30

        for i in range(11):  # Total number of rows in the layout
            window.grid_rowconfigure(i, weight=1)
            # Create two columns for each row
        window.grid_columnconfigure(i*2, weight=0)  # For labels
        window.grid_columnconfigure(i*2 + 1, weight=1)  # For entry fields

        # Basic Information
        first_name_label = tk.Label(window, text="FIRST NAME:", font=label_font_style)
        first_name_entry = tk.Entry(window, width=entry_width)
        first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        first_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        last_name_label = tk.Label(window, text="LAST NAME:", font=label_font_style)
        last_name_entry = tk.Entry(window, width=entry_width)
        last_name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        last_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        address_label = tk.Label(window, text="EMAIL ADDRESS:", font=label_font_style)
        address_entry = tk.Entry(window, width=entry_width)
        address_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        address_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        contact_number_label = tk.Label(window, text="CONTACT NUMBER:", font=label_font_style)
        contact_number_entry = tk.Entry(window, width=entry_width)
        contact_number_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        contact_number_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Entry fields for symptoms and vaccination
        symptoms_label = tk.Label(window, text="SYMPTOMS:", font=label_font_style)
        symptoms_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        self.cough_var = tk.BooleanVar()
        cough_checkbox = tk.Checkbutton(window, text="Cough", font=label_font_style, variable=self.cough_var, onvalue=True, offvalue=False)
        cough_checkbox.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

        self.fever_var = tk.BooleanVar()
        fever_checkbox = tk.Checkbutton(window, text="Fever", font=label_font_style, variable=self.fever_var, onvalue=True, offvalue=False)
        fever_checkbox.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

        self.breathing_var = tk.BooleanVar()
        breathing_checkbox = tk.Checkbutton(window, text="Breathing Difficulties", font=label_font_style, variable=self.breathing_var, onvalue=True, offvalue=False)
        breathing_checkbox.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)

        vaccination_label = tk.Label(window, text="VACCINATION:", font=label_font_style)
        vaccination_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)

        self.first_vaccine_var = tk.BooleanVar()
        first_vaccine_checkbox = tk.Checkbutton(window, text="1st Vaccine", font=label_font_style, variable=self.first_vaccine_var, onvalue=True, offvalue=False)
        first_vaccine_checkbox.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)

        self.second_vaccine_var = tk.BooleanVar()
        second_vaccine_checkbox = tk.Checkbutton(window, text="2nd Vaccine", font=label_font_style, variable=self.second_vaccine_var, onvalue=True, offvalue=False)
        second_vaccine_checkbox.grid(row=10, column=0, padx=10, pady=5, sticky=tk.W)

        self.booster_shot_var = tk.BooleanVar()
        booster_shot_checkbox = tk.Checkbutton(window, text="Booster Shot", font=label_font_style, variable=self.booster_shot_var, onvalue=True, offvalue=False)
        booster_shot_checkbox.grid(row=11, column=0, padx=10, pady=5, sticky=tk.W)
        
        # Save button
        save_button = tk.Button(window, text="SAVE", font=label_font_style, command=save_contact)
        save_button.grid(row=15, column=0, padx=10, pady=20, sticky=tk.EW)
        
         # Center the button at the bottom
        window.grid_rowconfigure(15, weight=1)
        window.grid_columnconfigure(0, weight=1)
        
        self.menu_window.withdraw()  # Hide the menu window while the "Add Contact" window is open

    def edit_contact(self):
        def edit_selected_contact():
            # Get the selected contact from the listbox
            selected_index = contact_listbox.curselection()
            if selected_index:
                selected_contact = self.new_contacts[selected_index[0]]
                edit_window.destroy()
                self.edit_selected_contact_fields(selected_contact, self.menu_window)
            else:
                messagebox.showinfo("Invalid Input", "Please select a contact to edit.")

        def cancel_edit():
            edit_window.destroy()
            self.show_menu()

        # Create the "Edit Contact" window
        edit_window = tk.Toplevel(self.menu_window)
        edit_window.title("Edit Contact")
        edit_window.geometry("1000x600")
        edit_window.resizable(False, False)

        # Create a frame to organize the layout of the listbox and the "Select" button
        frame = tk.Frame(edit_window)
        frame.pack(pady=10)

        # Get all contacts' full names for the listbox
        contact_names = [f"{contact[0]} {contact[1]}" for contact in self.new_contacts]

        # Listbox to display the contacts
        contact_listbox = tk.Listbox(edit_window, width=800, height=400, selectmode=tk.SINGLE)
        for name in contact_names:
            contact_listbox.insert(tk.END, name)
        contact_listbox.pack(pady=10)

        buttons_frame = tk.Frame(edit_window)
        buttons_frame.pack(pady=5)

        # Button to select the contact to edit
        select_button = tk.Button(frame, text="Select", command=edit_selected_contact)
        select_button.pack(side=tk.LEFT, pady=5)

        # Cancel button
        cancel_button = tk.Button(frame, text="Cancel", command=cancel_edit)
        cancel_button.pack(side=tk.LEFT, pady=5)

        # Hide the menu window while the "Edit Contact" window is open
        self.menu_window.withdraw()

    def edit_selected_contact_fields(self, contact, menu_window):
        def save_edited_contact(contact, fields):
            for option in edit_options:
                new_value = fields[option].get()
                if new_value:
                    contact[edit_options.index(option)] = new_value
            self.save_contacts()
            messagebox.showinfo("Success", "Contact updated successfully.")
            edit_window.destroy()
            menu_window.deiconify()

        def cancel_edit():
            edit_window.destroy()
            menu_window.deiconify()

        # Create the "Edit Contact Fields" window
        edit_window = tk.Toplevel(menu_window)
        edit_window.title("Edit Contact Fields")
        edit_window.geometry("1000x600")
        edit_window.resizable(False, False)
        edit_options = ["First Name", "Last Name", "Email Address", "Contact Number"]
        fields = {}

        # Entry fields for each contact field
        for option in edit_options:
            label = tk.Label(edit_window, text=option)
            label.pack(pady=5)
            entry = tk.Entry(edit_window)
            entry.pack(pady=5)
            entry.insert(0, contact[edit_options.index(option)])
            fields[option] = entry

        # Save and Cancel buttons
        save_button = tk.Button(edit_window, text="Save", command=lambda: save_edited_contact(contact, fields))
        cancel_button = tk.Button(edit_window, text="Cancel", command=cancel_edit)
        
        cancel_button.pack(side=tk.BOTTOM, pady=5)
        save_button.pack(side=tk.BOTTOM, pady=10)

    def delete_contact(self):
        def delete_selected_contact():
            # Get the selected contact from the listbox
            selected_index = contact_listbox.curselection()
            if selected_index:
                selected_contact = self.new_contacts[selected_index[0]]
                self.new_contacts.remove(selected_contact)  # Remove the contact from the new contacts list
                self.save_contacts()  # Save the updated contacts
                messagebox.showinfo("Success", "Contact deleted successfully.")
                delete_window.destroy()
                self.show_menu()
                self.menu_window.deiconify()
            else:
                messagebox.showinfo("Invalid Input", "Please select a contact to delete.")

        # Create the "Delete Contact" window
        delete_window = tk.Toplevel(self.menu_window)
        delete_window.title("Delete Contact")
        delete_window.geometry("1000x600")
        delete_window.resizable(False, False)

        # Get all contacts' full names for the listbox
        contact_names = [f"{contact[0]} {contact[1]}" for contact in self.new_contacts]

        # Listbox to display the contacts
        contact_listbox = tk.Listbox(delete_window, width=30, height=10, selectmode=tk.SINGLE)
        for name in contact_names:
            contact_listbox.insert(tk.END, name)
        contact_listbox.pack(pady=10)

        # Button to select the contact to delete
        delete_button = tk.Button(delete_window, text="Delete", command=delete_selected_contact)
        delete_button.pack(pady=5)

        # Hide the menu window while the "Delete Contact" window is open
        self.menu_window.withdraw()

    def view_contacts(self):
        self.menu_window.withdraw()

        view_window = tk.Toplevel(self.master)
        view_window.title("View Contacts")
        view_window.geometry("1000x600")
        view_window.resizable(False, False)

        tree = ttk.Treeview(view_window)
        tree["columns"] = ("First Name", "Last Name", "Email Address", "Contact Number","Symptoms", "First Vaccine", "Second Vaccine", "Booster Shot")
        tree.heading("#0", text="ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Email Address", text="Email Address")
        tree.heading("Contact Number", text="Contact Number")
        tree.heading("Symptoms", text="Symptoms")
        tree.heading("First Vaccine", text="First Vaccine")
        tree.heading("Second Vaccine", text="Second Vaccine")
        tree.heading("Booster Shot", text="Booster Shot")

        # Configure column widths
        tree.column("#0", width=20)
        tree.column("First Name", width=100)
        tree.column("Last Name", width=100)
        tree.column("Email Address", width=150)
        tree.column("Contact Number", width=100)
        tree.column("Symptoms", width=200)
        tree.column("First Vaccine", width=100)
        tree.column("Second Vaccine", width=100)
        tree.column("Booster Shot", width=100)

        # Delete existing entries in the Treeview
        tree.delete(*tree.get_children())

        # Insert data into the treeview
        for i, contact in enumerate(self.new_contacts):
            if len(contact) == 8:  # Check the length of the contact before unpacking
                first_name, last_name, address, contact_number, symptoms, first_vaccine, second_vaccine, booster_shot = contact
                symptoms_str = ", ".join(symptom for symptom, status in symptoms.items() if status)
                tree.insert("", tk.END, text=str(i + 1), values=(first_name, last_name, address, contact_number, symptoms_str, first_vaccine, second_vaccine, booster_shot))

        tree.pack()

        def close_view_window():
            view_window.destroy()
            self.show_menu()
            self.menu_window.deiconify()

        view_window.protocol("WM_DELETE_WINDOW", close_view_window)

    def search_contacts(self):
        self.menu_window.withdraw()  # Hide the menu window while the search window is open

        search_window = tk.Toplevel(self.master)
        search_window.title("Search Contact")
        search_window.geometry("1000x600")
        search_window.resizable(False, False)

        self.search_window = search_window

        entry_label = tk.Label(search_window, text="Enter search query:")
        entry_label.pack(pady=10)

        entry = tk.Entry(search_window)
        entry.pack()

        search_button = tk.Button(search_window, text="Search", command=lambda win=search_window: self.perform_search(None, entry.get(), win))
        search_button.pack(pady=10)

        search_window.protocol("WM_DELETE_WINDOW", self.close_search_window)

    def close_search_window(self):
        self.search_window.destroy()
        self.menu_window.deiconify()  # Show the menu window again
        self.menu_window.lift()

    def perform_search(self, search_criteria, search_query=None, search_window=None):
        if search_query:
            results = []
            for contact in self.new_contacts:
                if search_criteria is None or search_criteria == "Last Name" and search_query.lower() in contact[1].lower():
                    results.append(contact)
                elif search_criteria is None or search_criteria == "First Name" and search_query.lower() in contact[0].lower():
                    results.append(contact)
                elif search_criteria is None or search_criteria == "Address" and search_query.lower() in contact[2].lower():
                    results.append(contact)
                elif search_criteria is None or search_criteria == "Contact Number" and search_query.lower() in str(contact[3]):
                    results.append(contact)
            if results:
                self.show_search_results(results, search_window)
            else:
                messagebox.showinfo("No Results", "No contacts match the search query.")
        else:
            messagebox.showinfo("Invalid Input", "Search query is required.")

    def show_search_results(self, results, search_window):
        result_frame = tk.Frame(search_window)
        result_frame.pack(pady=10)

        tree = ttk.Treeview(result_frame)
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

        def view_selected_contact(event):
            selected_item = tree.selection()[0]
            selected_contact = results[int(tree.item(selected_item, "text")) - 1]
            self.show_contact_details(selected_contact)

        tree.bind("<Double-1>", view_selected_contact)

    def show_contact_details(self, contact):
        contact_window = tk.Toplevel(self.master)
        contact_window.title("Contact Details")
        contact_window.geometry("1000x600")
        contact_window.resizable(False, False)

        for i, field in enumerate(["First Name:", "Last Name:", "Address:", "Contact Number:"]):
            label = tk.Label(contact_window, text=field)
            label.grid(row=i, column=0)
            value = tk.Label(contact_window, text=contact[i])
            value.grid(row=i, column=1)

    def on_exit(self):
        self.save_contacts()
        # Close the entire application by destroying the root window
        self.master.destroy()

    # Destroy the menu window and show the main window
    def close_menu_window(self):
        self.menu_window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    gui = COVID_Contacts_Information(root)
    root.mainloop()
