from add_contact import add_contact
from remove_contact import remove_contact
from save_contacts import save_contacts
from search_contact import search_contact
from view_contacts import view_contacts
from load_contacts import load_contacts

def main():
    contact_book = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Save Contacts")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter phone address: ")
            add_contact(contact_book, name, phone,email,address)

        elif choice == "2":
            name = input("Enter the name of the contact to remove: ")
            remove_contact(contact_book, name)

        elif choice == "3":
            view_contacts(contact_book)

        elif choice == "4":
            save_contacts(contact_book)
        
        elif choice == "5":
            name = input("Enter the name of the contact to search: ")
            search_contact(contact_book, name)
        
        elif choice == "6":
            save_contacts(contact_book)  # Save before exiting
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()