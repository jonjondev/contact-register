"""
ContactRegister HTML Module

This script defines display methods for the HTML format:
    * display_contacts - displays a list of contacts in HTML
    * contacts_to_list_items - formats list of contacts as an HTML list

This script should be imported wherever needed as module.
"""

import os
import webbrowser


# Define module constants
DATA_FILE = "data/contacts.html"


def display_contacts(contacts) -> None:
    """
    A module function to display contacts in HTML, opening the
    generated file in the default web-browser
    ...
    Parameters
    ----------
    contacts : [Contact]
        a list of contact objects to display
    """
    # Open the specified file for writing
    with open(DATA_FILE, 'w', newline='') as file:
        # Write the structure of the HTML file populated with contacts
        file.write('<html>\n'
                   '\t<head>\n'
                   '\t\t<title>Data Value</title>\n'
                   '\t</head>\n'
                   '\t<body>\n'
                   '\t\t<h1>All Contacts</h1>\n'
                   '\t\t<ul>\n'
                   f'{contacts_to_list_items(contacts)}\n'
                   '\t\t</ul>\n'
                   '\t</body>\n'
                   '</html>')
    print(f'Created new file at {DATA_FILE}')
    print('Opening in browser...')
    # Open the file for viewing in the user's default web-browser
    webbrowser.open_new('file://' + os.path.realpath(DATA_FILE))


def contacts_to_list_items(contacts) -> str:
    """
    A module helper function to convert a list of contacts to
    a string of HTML unordered list items
    ...
    Parameters
    ----------
    contacts : [Contact]
        a list of contact objects to transform
    ...
    Returns
    -------
    str
        a string containing the formatted items
    """
    # Generate a list of HTML <li> items and join them as a string
    return "\n\t\t\t".join([f'<li>{contact}</li>' for contact in contacts])
