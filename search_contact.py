def search_contact(contact_book, name):
    if name in contact_book:
        print(f"Found contact for {name}: {contact_book[name]}")
    else:
        print(f"No contact found for {name}.")