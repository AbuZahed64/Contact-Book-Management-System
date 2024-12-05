
import json

def save_contacts(contact_book, filename="contacts.json"):
    try:
        with open(filename, "w") as file:
            json.dump(contact_book, file)
            print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")
