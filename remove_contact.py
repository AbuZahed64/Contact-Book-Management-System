def remove_contact(contact_book, name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} removed successfully.")
    else:
        print(f"No contact found for {name}.")