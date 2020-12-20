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
    """
    A module function to add a new contact
    ...
    Parameters
    ----------
    name : str
        the contact's full name
    address : str
        the contact's address
    phone : str
        the contact's phone number
    ...
    Returns
    -------
    Contact
        the newly created contact object
    """
    # Create a new contact, add it to the list, and return it
    contact = Contact(name, address, phone)
    contacts.append(contact)
    return contact


def get_all_contacts() -> [Contact]:
    """
    A module function to return all contacts
    ...
    Returns
    -------
    [Contact]
        a list of all contact objects
    """
    # Return all contacts
    return contacts


def search_contacts(query_field, query) -> [Contact]:
    # TODO implement different query format and display on multiple fields (++comment)
    return fnmatch.filter([getattr(contact, query_field) for contact in contacts], query)


def display_contacts(display_format) -> None:
    """
    A module function to display all contacts
    ...
    Parameters
    ----------
    display_format : str
        the name of the display format to use (text, html, etc.)
    """
    # Dynamically import the specified display format module and run its display method
    importlib.import_module(f'display.{display_format}').display(contacts)


def export_contacts(export_format) -> str:
    """
    A module function to export all contacts
    ...
    Parameters
    ----------
    export_format : str
        the name of the export format to use (csv, json, etc.)
    """
    # Dynamically import the specified export format module and run its export method
    return importlib.import_module(f'serialisation.{export_format}').export(contacts)


def run_interactive_session():
    """
    A module function to start an interactive CLI session to operate
    the script's API functionality.

    The function defines the following commands:
        * add - add a new contact
        * list - list all contacts
        * search - filter contacts via globbing
        * display - display contacts in a specified format
        * export - export contacts to a specified format
        * help/? - display help information
        * quit/q - quit the interactive session
    """

    # Display session header text for user
    print('ContactRegister 1.0.0 (interactive console session)\n'
          'Type "help" or "?" for more information.')

    # Run the loop while receiving user input
    while True:
        # Get a user-supplied command as a string
        command = input("Type a command: ").strip()

        # Match the supplied command to its relevant interactive functionality
        # ADD CONTACT
        if command == "add":
            # Get contact info from user input
            name = input("Name: ").strip()
            address = input("Address: ").strip()
            phone = input("Phone: ").strip()
            # Create the contact and notify the user
            contact = add_contact(name, address, phone)
            print(f'Successfully added new contact: {contact}')

        # LIST ALL CONTACTS
        elif command == "list":
            # Get a list of all contacts and display them
            all_contacts = get_all_contacts()
            print(f'Showing {len(all_contacts)} contacts...')
            [print(contact) for contact in all_contacts]

        # SEARCH CONTACTS
        elif command == "search":
            # TODO comment this section
            query_fields = Contact.supported_search_fields
            helpers.display_command_options(query_fields, "Query field options:")
            selected_field = helpers.get_option_selection(query_fields, prompt="Field: ")
            query = input("Query: ").strip()
            results = search_contacts(selected_field, query)
            print(f'Showing {len(results)} results...')
            [print(contact) for contact in results]

        # DISPLAY CONTACTS
        elif command == "display":
            # TODO comment this section
            display_formats = display.get_formats()
            helpers.display_command_options(display_formats, "Display format options:")
            selected_format = helpers.get_option_selection(display_formats, prompt="Format: ")
            display_contacts(selected_format)

        # EXPORT CONTACTS
        elif command == "export":
            # TODO comment this section
            export_formats = serialisation.get_formats()
            helpers.display_command_options(export_formats, "Export format options:")
            selected_format = helpers.get_option_selection(export_formats, prompt="Format: ")
            export_file = export_contacts(selected_format)
            print(f'Exported {len(contacts)} contacts to {export_file}')

        # VIEW HELP
        elif command in {"help", "?"}:
            # Display help menu text
            print("------------------------------ HELP MENU ------------------------------\n"
                  "The following commands are provided by this program:\n"
                  "    * add     - ADD CONTACT: add a new contact\n"
                  "    * list    - LIST ALL CONTACTS: view all contacts\n"
                  "    * search  - SEARCH CONTACTS: search through contacts with globbing\n"
                  "    * display - DISPLAY CONTACTS: display contacts in a given format\n"
                  "    * export  - EXPORT CONTACTS: export contacts to a given format\n"
                  "    * ?/help  - HELP: open help page\n"
                  "    * q/quit  - QUIT: quit the interactive session\n")

        # QUIT
        elif command in {"quit", "q"}:
            # Exit the session loop
            break

        # DEFAULT CASES
        elif command == "":
            # Notify the user of blank input
            print('Need help? Type "?" for a list of available commands')
        else:
            # Notify the user of unknown input
            print(f'No such command "{command}", type "?" for a list of available commands')


# Run module as script if it's invoked as main
if __name__ == '__main__':
    run_interactive_session()
