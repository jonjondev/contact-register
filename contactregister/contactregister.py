from models.Contact import Contact
import serialisation
import fnmatch
import display
import helpers


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
    query_fields = Contact.supported_search_fields
    helpers.display_command_options(query_fields, "Query field options:")
    field = int(input(f'Field: '))  # TODO fix explicit int conversion
    query = input("Query: ")
    matches = fnmatch.filter([getattr(contact, query_fields[field]) for contact in contacts], query)
    [print(contact) for contact in matches]


def display_contacts() -> None:
    display_formats = display.get_formats()
    helpers.display_command_options(display_formats, "Display format options:")
    display_format = int(input(f'Format: '))  # TODO fix explicit int conversion
    print(f'<display all contacts in {display_formats[display_format]}>')


def export_contacts() -> None:
    export_formats = serialisation.get_formats()
    helpers.display_command_options(export_formats, "Export format options:")
    export_format = int(input(f'Format: '))  # TODO fix explicit int conversion
    print(f'<export all contacts to {export_formats[export_format]}>')


def view_help() -> None:
    print("<display list of available commands>")


def run_interactive():
    # Run the loop while receiving user input
    while True:
        # Get a user-supplied command as a string
        command = input("Type a command: ")

        # Match the supplied command to its relevant interactive functionality
        # TODO update to separate "API" methods from interactive functions
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


# Run module as script if is invoked as main
if __name__ == '__main__':
    run_interactive()
