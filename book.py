import json

class cBook:
        
    def __init__(self):
        self.contacts = {"Name": "Phone No."}
    

    def Display(self):
        for key, value in self.contacts.items():
            print(key, value)

    def AddC(self):
        aName = input("Name of New Contact: ")
        aNumber = (input("Give phone number: "))
        if len(str(aNumber)) != 10:
            print("This is not valid input numbers are 10 digits")
        else:
            print(f"Adding {aName} with the No. {aNumber}")
        self.contacts[aName] = aNumber

    def RemoveC(self):
        name = input("Name of Contact you would like to Remove: ")
        if name in self.contacts:
            print(f"Name: {name}, No: {self.contacts[name]}")
            confirm = input("Do you want to delete it?: ").lower()
            if confirm == 'y' or confirm == 'yes':
                self.contacts.pop(name)
                print("Contact removed")
            else:
                print("Ok :)")
        else:
            print("Contact not found")
    def Search(self):
        name = input("Name of Contact you would like to Search: ")
        if name in self.contacts:
            print(f"Name: {name}, No: {self.contacts[name]}")
        else:
            print("Contact not found")

    def Save(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f)

    def Load(self):
        with open("contacts.json", "r") as f:
            self.contacts = json.load(f)
        