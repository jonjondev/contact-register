"""
ContactRegister HTML Module

This script defines display methods for the HTML format:
    * display - displays a list of contacts in HTML

This script should be imported wherever needed as module.
"""

import os
import webbrowser


# Define module constants
DATA_FILE = "data/contacts.html"


def display(contacts) -> None:
    """
    A module function to display contacts in HTML
    ...
    Parameters
    ----------
    contacts : [Contact]
        a list of contact objects to display
    """
    # TODO Comment this function
    with open(DATA_FILE, 'w', newline='') as file:
        file.write('<html>\n'
                   '\t<head>\n'
                   '\t\t<title>Data Value</title>\n'
                   '\t</head>\n'
                   '\t<body>\n'
                   '\t\t<h1>All Contacts</h1>\n'
                   '\t\t<ul>'
                   f'{contacts_to_list_items(contacts)}\n'
                   '\t\t</ul>\n'
                   '\t</body>\n'
                   '</html>')
    print(f'Created new file at {DATA_FILE}')
    print('Opening in browser...')
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
    # TODO Comment this function
    return "".join([f'\n\t\t\t<li>{contact}</li>' for contact in contacts])
