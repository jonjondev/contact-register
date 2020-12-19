"""
ContactRegister Main Script

This script provides an API to the contactregister system, which
allows for the creation, modification, display, and export of contacts
to various formats specified in its submodules.

This script exposes the following API functions:
    * add_contact - adds a new contact to the system
    * get_all_contacts - returns all current system contacts
    * search_contacts - returns contacts based on a search query
    * display_contacts - displays all contacts in a specified format
    * export_contacts - exports all contacts to a specified format

This file can be imported as a module and additionally offers an
interactive session mode for CLI operation using the following function:
    * run_interactive_session - starts the interactive CLI session

If the file is invoked directly (as main) it will launch the interactive
mode by default.
"""

from models.Contact import Contact
import serialisation
import importlib
import fnmatch
import display
import helpers


# Initialise contact list
contacts = []


def add_contact(name, address, phone) -> Contact:
    contact = Contact(name, address, phone)
    contacts.append(contact)
    return contact


def get_all_contacts() -> [Contact]:
    return contacts


def search_contacts(query_field, query) -> [Contact]:
    return fnmatch.filter([getattr(contact, query_field) for contact in contacts], query)


def display_contacts(display_format) -> None:
    importlib.import_module(f'display.{display_format}').display(contacts)


def export_contacts(export_format) -> None:
    importlib.import_module(f'serialisation.{export_format}').export(contacts)


def run_interactive_session():
    # Run the loop while receiving user input
    while True:
        # Get a user-supplied command as a string
        command = input("Type a command: ")

        # Match the supplied command to its relevant interactive functionality:
        # ADD CONTACT
        if command in {"add contact", "add"}:
            name = input("Name: ")
            address = input("Address: ")
            phone = input("Phone: ")
            contact = add_contact(name, address, phone)
            print(f'Successfully added new contact: {contact}')

        # LIST ALL CONTACTS
        elif command in {"list contacts", "list"}:
            [print(contact) for contact in get_all_contacts()]

        # SEARCH CONTACTS
        elif command in {"search contacts", "search"}:
            query_fields = Contact.supported_search_fields
            helpers.display_command_options(query_fields, "Query field options:")
            field = int(input(f'Field: '))  # TODO fix explicit int conversion
            query = input("Query: ")
            [print(contact) for contact in search_contacts(query_fields[field], query)]

        # DISPLAY CONTACTS
        elif command in {"display contacts", "display"}:
            display_formats = display.get_formats()
            helpers.display_command_options(display_formats, "Display format options:")
            display_format = int(input(f'Format: '))  # TODO fix explicit int conversion
            display_contacts(display_formats[display_format])

        # EXPORT CONTACTS
        elif command in {"export contacts", "export"}:
            export_formats = serialisation.get_formats()
            helpers.display_command_options(export_formats, "Export format options:")
            export_format = int(input(f'Format: '))  # TODO fix explicit int conversion
            export_contacts(export_formats[export_format])

        # VIEW HELP
        elif command in {"help", "?"}:
            print("<display list of available commands>")

        # QUIT
        elif command in {"quit", "q"}:
            break

        # DEFAULT CASES
        elif command == "":
            print('Need help? Type "?" for a list of available commands')
        else:
            print(f'No such command "{command}", type "?" for a list of available commands')


# Run module as script if it's invoked as main
if __name__ == '__main__':
    run_interactive_session()
