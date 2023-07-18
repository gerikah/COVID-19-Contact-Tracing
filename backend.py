import csv

# create the class
class COVID_Contacts_Informations:
    def __init__(self):
        self.all_contacts = []

    def contacts(self): # to load the contacts saved in csv
        try:
            with open("covid_contacts_record.csv") as file:
