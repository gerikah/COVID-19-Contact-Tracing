import csv

# create the class
class COVID_Contacts_Informations:
    def __init__(self):
        self.all_contacts = []

    # reading contact
    def contacts(self): # to load the contacts saved in csv
        try:
            with open("covid_contacts_record.csv", mode="r") as file:
                reader = csv.reader(file) # set read mode using csv reader
                self.all_contacts = list(reader) # save sa all_contacts
        except FileNotFoundError: # exception handling if file is not found
            pass
        except Exception as e: # error message
            raise Exception(f"Failed to load address book: {str(e)}")
        
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

    # save contact
    # editing existing contact
    # deleting contact
    # search contact from the file

    

