import fnmatch
from models.Contact import Contact


# Initialise contact list
contacts = []


def add_contact() -> None:
    name = input("Name: ")
    address = input("Address: ")
    phone = input("Phone: ")
    contact = Contact(name, address, phone)
    contacts.append(contact)
    print(f'Successfully added new contact: {contact}')


def list_contacts() -> None:
    [print(contact) for contact in contacts]


def search_contacts() -> None:
    contact_fields = {"name", "address", "phone"}
    field = input(f'Field ({"/".join(contact_fields)}): ')
    query = input("Query: ")
    matches = fnmatch.filter([getattr(contact, field) for contact in contacts], query)
    [print(contact) for contact in matches]


def display_contacts() -> None:
    display_formats = {"text", "html"}
    display_format = input(f'Format ({"/".join(display_formats)}): ')
    print(f'<display all contacts in {display_format}>')


def export_contacts() -> None:
    export_formats = {"csv", "json"}
    export_format = input(f'Format ({"/".join(export_formats)}): ')
    print(f'<export all contacts to {export_format}>')


def view_help() -> None:
    print("<display list of available commands>")


def run_interactive():
    # Run the loop while receiving user input
    while True:
        # Get a user-supplied command as a string
        command = input("Type a command: ")

        # Match the supplied command to its relevant interactive functionality
        if command in {"add contact", "add"}:
            add_contact()
        elif command in {"list contacts", "list"}:
            list_contacts()
        elif command in {"search contacts", "search"}:
            search_contacts()
        elif command in {"display contacts", "display"}:
            display_contacts()
        elif command in {"export contacts", "export"}:
            export_contacts()
        elif command in {"help", "?"}:
            view_help()
        elif command in {"quit", "q"}:
            break
        elif command == "":
            print('Need help? Type "?" for a list of available commands')
        else:
            print(f'No such command "{command}", type "?" for a list of available commands')


if __name__ == '__main__':
    run_interactive()
