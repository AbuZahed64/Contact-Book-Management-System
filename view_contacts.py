def view_contacts(contact_book):
    if contact_book:
        print("Contacts:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")