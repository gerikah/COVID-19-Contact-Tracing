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
        
