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

    def load_contacts_from_file(self):  # to load the contacts saved in csv
        try:
            with open("covid_contacts_record.csv", mode="r") as file:
                reader = csv.reader(file)  # set read mode using csv reader
                self.all_contacts = list(reader)  # save sa all_contacts
                self.new_contacts = self.all_contacts.copy()
        except FileNotFoundError:  # exception handling if file is not found
            self.save_contacts()
        except Exception as e:  # error message
            raise Exception(f"Failed to load contact book: {str(e)}")

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
            # If the menu window doesn't exist
            self.menu_window = tk.Toplevel()
            self.menu_window.title("SAFE TRACK - MENU")
            self.menu_window.geometry("1100x600")
            self.menu_window.configure(bg="#370607")
            self.menu_window.protocol("WM_DELETE_WINDOW", self.on_exit)
            self.create_menu_content()

    def add_contact(self):
        self.menu_window.withdraw()
        self.add_window = tk.Toplevel()
        self.add_window.title("SAFE TRACK - ADD CONTACT")
        self.add_window.geometry("1000x600")
        self.add_window.configure(bg="#370607")

        # Font Style
        label_font_style = tkfont.Font(family="Poppins", size=12, weight="bold")

        # Add Contact Form Labels
        label_x = 100
        label_y = 100
        tk.Label(self.add_window, text="First Name:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y, anchor=tk.W)
        tk.Label(self.add_window, text="Last Name:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y + 40, anchor=tk.W)
        tk.Label(self.add_window, text="Email Address:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y + 80, anchor=tk.W)
        tk.Label(self.add_window, text="Contact Number:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y + 120, anchor=tk.W)

        # Add Contact Form Entry Fields
        self.first_name_entry = tk.Entry(self.add_window, width=30, font=label_font_style)
        self.first_name_entry.place(x=label_x + 180, y=label_y, anchor=tk.W)
        self.last_name_entry = tk.Entry(self.add_window, width=30, font=label_font_style)
        self.last_name_entry.place(x=label_x + 180, y=label_y + 40, anchor=tk.W)
        self.email_entry = tk.Entry(self.add_window, width=30, font=label_font_style)
        self.email_entry.place(x=label_x + 180, y=label_y + 80, anchor=tk.W)
        self.contact_number_entry = tk.Entry(self.add_window, width=30, font=label_font_style)
        self.contact_number_entry.place(x=label_x + 180, y=label_y + 120, anchor=tk.W)

        # Symptoms Section
        tk.Label(self.add_window, text="Symptoms:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y + 160, anchor=tk.W)
        symptoms_list = ["Fever", "Cough", "Shortness of Breath", "Fatigue", "Muscle or Body Aches", "Headache", "Loss of Taste or Smell", "Sore Throat"]
        self.symptoms_status = {symptom: tk.BooleanVar() for symptom in symptoms_list}
        row = 0
        for symptom, status_var in self.symptoms_status.items():
            tk.Checkbutton(self.add_window, text=symptom, variable=status_var, bg="#370607", fg="white", font=label_font_style).place(x=label_x + 180, y=label_y + 160 + (row * 30), anchor=tk.W)
            row += 1

        # Vaccination Status
        tk.Label(self.add_window, text="Vaccination Status:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y + 340, anchor=tk.W)
        self.vaccine_status = tk.BooleanVar()
        tk.Checkbutton(self.add_window, text="Vaccinated", variable=self.vaccine_status, bg="#370607", fg="white", font=label_font_style).place(x=label_x + 180, y=label_y + 340, anchor=tk.W)

        # Save Button
        button_x = 300
        button_y = 500
        tk.Button(self.add_window, text="Save Contact", font=("Poppins", 15, "bold"), command=self.save_contact, bg="#006B65", fg="#370607").place(x=button_x, y=button_y, anchor=tk.CENTER)

        self.add_window.protocol("WM_DELETE_WINDOW", self.on_close_add)

    def save_contact(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()
        contact_number = self.contact_number_entry.get().strip()

        if not first_name or not last_name or not email or not contact_number:
            messagebox.showerror("Error", "Please fill all the required fields.")
            return

        # Validate email address
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Invalid email address.")
            return

        # Validate contact number
        contact_number_pattern = r"^[0-9]{10}$"
        if not re.match(contact_number_pattern, contact_number):
            messagebox.showerror("Error", "Invalid contact number. Please enter 10 digits without spaces or special characters.")
            return

        # Save symptoms and vaccination status
        symptoms_str = self.save_symptoms(self.symptoms_status)
        vaccine_status_str = self.save_vaccination_status(self.vaccine_status.get())

        # Save the contact to the list
        contact = [first_name, last_name, email, contact_number, symptoms_str, vaccine_status_str]
        self.new_contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully.")

        # Clear the entry fields
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.contact_number_entry.delete(0, tk.END)
        for symptom in self.symptoms_status.values():
            symptom.set(False)
        self.vaccine_status.set(False)

    def save_symptoms(self, symptoms):
        symptoms_str = ", ".join(symptom for symptom, status in symptoms.items() if status)
        return symptoms_str

    def save_vaccination_status(self, vaccines):
        return "Yes" if vaccines else "No"

    def on_close_add(self):
        self.add_window.withdraw()
        self.show_menu()

        self.add_window.protocol("WM_DELETE_WINDOW", self.on_close_add)

    def edit_contact(self):
        self.menu_window.withdraw()
        self.edit_window = tk.Toplevel()
        self.edit_window.title("SAFE TRACK - EDIT CONTACT")
        self.edit_window.geometry("1000x600")
        self.edit_window.configure(bg="#370607")

        # Font Style
        label_font_style = tkfont.Font(family="Poppins", size=12, weight="bold")

        # Edit Contact Form Labels
        label_x = 100
        label_y = 100
        tk.Label(self.edit_window, text="Select Contact:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y, anchor=tk.W)

        # Edit Contact Dropdown
        self.selected_contact = tk.StringVar()
        self.selected_contact.set("Select")
        contact_names = [f"{contact[0]} {contact[1]}" for contact in self.new_contacts]
        self.contact_dropdown = tk.OptionMenu(self.edit_window, self.selected_contact, *contact_names)
        self.contact_dropdown.config(width=30, font=label_font_style, bg="#006B65", fg="#370607")
        self.contact_dropdown.place(x=label_x + 180, y=label_y - 5, anchor=tk.W)

        # Edit Contact Form Entry Fields
        self.first_name_entry_edit = tk.Entry(self.edit_window, width=30, font=label_font_style)
        self.first_name_entry_edit.place(x=label_x + 180, y=label_y + 40, anchor=tk.W)
        self.last_name_entry_edit = tk.Entry(self.edit_window, width=30, font=label_font_style)
        self.last_name_entry_edit.place(x=label_x + 180, y=label_y + 80, anchor=tk.W)
        self.email_entry_edit = tk.Entry(self.edit_window, width=30, font=label_font_style)
        self.email_entry_edit.place(x=label_x + 180, y=label_y + 120, anchor=tk.W)
        self.contact_number_entry_edit = tk.Entry(self.edit_window, width=30, font=label_font_style)
        self.contact_number_entry_edit.place(x=label_x + 180, y=label_y + 160, anchor=tk.W)

        # Symptoms Section
        tk.Label(self.edit_window, text="Symptoms:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y + 200, anchor=tk.W)
        symptoms_list = ["Fever", "Cough", "Shortness of Breath", "Fatigue", "Muscle or Body Aches", "Headache", "Loss of Taste or Smell", "Sore Throat"]
        self.symptoms_status_edit = {symptom: tk.BooleanVar() for symptom in symptoms_list}
        row = 0
        for symptom, status_var in self.symptoms_status_edit.items():
            tk.Checkbutton(self.edit_window, text=symptom, variable=status_var, bg="#370607", fg="white", font=label_font_style).place(x=label_x + 180, y=label_y + 200 + (row * 30), anchor=tk.W)
            row += 1

        # Vaccination Status
        tk.Label(self.edit_window, text="Vaccination Status:", font=label_font_style, bg="#370607", fg="white").place(x=label_x, y=label_y + 400, anchor=tk.W)
        self.vaccine_status_edit = tk.BooleanVar()
        tk.Checkbutton(self.edit_window, text="Vaccinated", variable=self.vaccine_status_edit, bg="#370607", fg="white", font=label_font_style).place(x=label_x + 180, y=label_y + 400, anchor=tk.W)

        # Load Contact Details Button
        button_x = 300
        button_y = 500
        tk.Button(self.edit_window, text="Load Contact Details", font=("Poppins", 15, "bold"), command=self.load_contact_details, bg="#006B65", fg="#370607").place(x=button_x, y=button_y, anchor=tk.CENTER)

        self.edit_window.protocol("WM_DELETE_WINDOW", self.on_close_edit)

    def load_contact_details(self):
        selected_contact_name = self.selected_contact.get()
        if selected_contact_name == "Select":
            messagebox.showerror("Error", "Please select a contact to edit.")
            return

        for contact in self.new_contacts:
            contact_name = f"{contact[0]} {contact[1]}"
            if selected_contact_name == contact_name:
                self.first_name_entry_edit.delete(0, tk.END)
                self.first_name_entry_edit.insert(0, contact[0])
                self.last_name_entry_edit.delete(0, tk.END)
                self.last_name_entry_edit.insert(0, contact[1])
                self.email_entry_edit.delete(0, tk.END)
                self.email_entry_edit.insert(0, contact[2])
                self.contact_number_entry_edit.delete(0, tk.END)
                self.contact_number_entry_edit.insert(0, contact[3])

                # Load symptoms
                self.load_symptoms(self.symptoms_status_edit, contact[4])

                # Load vaccination status
                self.vaccine_status_edit.set(True if contact[5] == "Yes" else False)

                break

    def load_symptoms(self, symptoms_status, symptoms_str):
        selected_symptoms = symptoms_str.split(", ")
        for symptom, status_var in symptoms_status.items():
            status_var.set(symptom in selected_symptoms)
    
    def on_close_edit(self):
        self.edit_window.withdraw()
        self.show_menu()

        self.edit_window.protocol("WM_DELETE_WINDOW", self.on_close_edit)

    def delete_contact(self):
        def delete_selected_contact():
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
        delete_window.geometry("400x200")
        delete_window.resizable(False, False)

        # Get all contacts' full names for the listbox
        contact_names = [f"{contact[0]} {contact[1]}" for contact in self.new_contacts]

        # Listbox to display the contacts
        contact_listbox = tk.Listbox(delete_window, width=40, height=10, selectmode=tk.SINGLE)
        for name in contact_names:
            contact_listbox.insert(tk.END, name)
        contact_listbox.pack(pady=10)

        # Button to select the contact to delete
        delete_button = tk.Button(delete_window, text="Delete", command=delete_selected_contact)
        delete_button.pack(pady=10)

        self.menu_window.withdraw()  # Hide the menu window while the "Delete Contact" window is open

    def view_contacts(self):
        self.menu_window.withdraw()

        view_window = tk.Toplevel(self.master)
        view_window.title("View Contacts")
        view_window.geometry("600x400")
        view_window.resizable(False, False)

        tree = ttk.Treeview(view_window)
        tree["columns"] = ("First Name", "Last Name", "Email Address", "Contact Number")
        tree.heading("#0", text="ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Email Address", text="Email Address")
        tree.heading("Contact Number", text="Contact Number")

        # Configure column widths
        tree.column("#0", width=50)
        tree.column("First Name", width=100)
        tree.column("Last Name", width=100)
        tree.column("Email Address", width=200)
        tree.column("Contact Number", width=100)

        # Insert data into the treeview
        for i, contact in enumerate(self.new_contacts):
            first_name, last_name, address, contact_number = contact[:4]
            tree.insert("", tk.END, text=str(i + 1), values=(first_name, last_name, address, contact_number))

        tree.pack()

        def view_selected_contact(event):
            selected_item = tree.selection()[0]
            selected_contact = self.new_contacts[int(tree.item(selected_item, "text")) - 1]
            self.show_contact_details(selected_contact)

        tree.bind("<Double-1>", view_selected_contact)

        def close_view_window():
            view_window.destroy()
            self.show_menu()
            self.menu_window.deiconify()

        view_window.protocol("WM_DELETE_WINDOW", close_view_window)



    def search_contacts(self):
        search_window = tk.Toplevel(self.menu_window)
        search_window.title("Search Contacts")
        search_window.geometry("400x200")
        search_window.resizable(False, False)

        label = tk.Label(search_window, text="Search by:", font=("Poppins", 12))
        label.pack(pady=10)

        search_criteria = tk.StringVar()
        search_criteria.set("First Name")
        options = ["First Name", "Last Name", "Email Address", "Contact Number"]

        criteria_menu = tk.OptionMenu(search_window, search_criteria, *options)
        criteria_menu.pack(pady=10)

        entry_label = tk.Label(search_window, text="Enter search query:", font=("Poppins", 12))
        entry_label.pack(pady=10)

        entry = tk.Entry(search_window)
        entry.pack(pady=10)

        search_button = tk.Button(search_window, text="Search", font=("Poppins", 12),
                                command=lambda: self.perform_search(search_criteria.get(), entry.get(), search_window))
        search_button.pack(pady=10)

        self.menu_window.withdraw()  # Hide the menu window while the search window is open

    def perform_search(self, search_criteria, search_query, search_window):
        if not search_query:
            messagebox.showerror("Error", "Search query cannot be empty.")
            return

        results = []
        for contact in self.new_contacts:
            if search_criteria == "First Name" and search_query.lower() in contact[0].lower():
                results.append(contact)
            elif search_criteria == "Last Name" and search_query.lower() in contact[1].lower():
                results.append(contact)
            elif search_criteria == "Email Address" and search_query.lower() in contact[2].lower():
                results.append(contact)
            elif search_criteria == "Contact Number" and search_query.lower() in str(contact[3]):
                results.append(contact)

        if results:
            self.show_search_results(results, search_window)
        else:
            messagebox.showinfo("No Results", "No contacts match the search query.")

    def show_search_results(self, results, search_window):
        search_window.withdraw()

        results_window = tk.Toplevel(self.menu_window)
        results_window.title("Search Results")
        results_window.geometry("800x500")
        results_window.resizable(False, False)

        tree = ttk.Treeview(results_window)
        tree["columns"] = ("First Name", "Last Name", "Email Address", "Contact Number")
        tree.heading("#0", text="ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Email Address", text="Email Address")
        tree.heading("Contact Number", text="Contact Number")

        # Configure column widths
        tree.column("#0", width=50)
        tree.column("First Name", width=150)
        tree.column("Last Name", width=150)
        tree.column("Email Address", width=200)
        tree.column("Contact Number", width=150)

        # Insert data into the treeview
        for i, contact in enumerate(results):
            tree.insert("", tk.END, text=str(i + 1), values=(contact[0], contact[1], contact[2], contact[3]))

        tree.pack(pady=10)

        def view_selected_contact(event):
            selected_item = tree.selection()[0]
            selected_contact = results[int(tree.item(selected_item, "text")) - 1]
            self.show_contact_details(selected_contact)

        tree.bind("<Double-1>", view_selected_contact)

        def close_results_window():
            results_window.destroy()
            self.menu_window.deiconify()  # Show the menu window again
            self.menu_window.lift()

        results_window.protocol("WM_DELETE_WINDOW", close_results_window)

    def on_close_search(self):
        self.search_window.withdraw()
        self.show_menu()

    def on_exit(self):
        self.save_contacts()
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    COVID_Contacts_Information(root)
    root.mainloop()
