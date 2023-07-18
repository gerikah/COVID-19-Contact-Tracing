import csv

# create the class
class COVID_Contacts_Informations:
    def __init__(self):
        self.all_contacts = []

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
    # save contact
    # editing existing contact
    # deleting contact
    # search contact from the file
    
    

