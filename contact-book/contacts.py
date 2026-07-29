#import json module
import json

#define filename and a "load contacts" function
FILENAME = "contacts.json"
def load_contacts():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#write a "save contacts" function
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

#load contacts at the start of the program
contacts = load_contacts()

#build the menu loop
while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Remove contacts")
    print("4. Exit")
    choice = input("Choose an option: ")
    #handle "Add contact"
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contact = {"name": name, "phone": phone, "email": email}
        contacts.append(contact)
        save_contacts(contacts)
        print(f"Added {name}")
    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        else:
            for i, c in enumerate(contacts):
                print(f"{i + 1}. {c['name']} - {c['phone']} - {c['email']}")
    elif choice == "3":
        if not contacts:
            print("No contacts to remove")
        else:
            for i, c in enumerate(contacts):
                print(f"{i + 1}. {c['name']}")
            index = int(input("Enter contact number to remove: ")) - 1
            if 0 <= index < len(contacts):
                removed = contacts.pop(index)
                save_contacts(contacts)
                print(f"Removed {removed['name']}")
            else:
                print("Invalid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else: print("Invalid option, try again.")