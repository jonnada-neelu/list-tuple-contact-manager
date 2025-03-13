# Contact manager application
# Contact Manager Application

contacts = []
def add_contact(name, phone, email):
    for contact in contacts:
        if contact[0] == name:
            print("Contact with this name already exists!")
            return
    contacts.append((name, phone, email))
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    print("\nList of Contacts:")
    for i in range(1, len(contacts) + 1):  
        contact = contacts[i - 1]
        name, phone, email = contact
        print(f"{i}. {name} - {phone} - {email}")

def search_contact(name):
    for contact in contacts:
        contact_name, phone, email = contact
        if contact_name == name:
            print(f"Contact Found: {contact_name} - {phone} - {email}")
            return
    print("Contact not found!")

def update_contact(name, email_id):
    global contacts
    for i in range(len(contacts)):  
        contact = contacts[i]
        contact_name, phone, email_id = contact
        if contact_name == name:
            contacts[i] = (contact_name, phone, email_id)
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact(name):
    """Deletes a contact by name."""
    global contacts
    for contact in contacts:
        contact_name = contact
        if contact_name == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

def main():
    while True:
        print("\nWelcome to Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            email_id = input("Enter new Email ID: ")
            update_contact(name, email_id)
        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
