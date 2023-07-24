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
                writer.writerows(self.all_contacts + self.new_contacts)
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

    

