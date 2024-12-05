from prevent_duplicate import prevent_duplicate

def add_contact(contact_book, name, email, phone, address):
 
    if prevent_duplicate(contact_book, name):
        contact_book[name] = {
            "email": email,
            "phone": phone,
            "address": address
        }
        print(f"Contact for {name} added successfully.")
    else:
        print(f"Contact with name {name} already exists.")