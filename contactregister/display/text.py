"""
ContactRegister Text Module

This script defines display methods for the Text format:
    * display_contacts - displays a list of contacts in output text

This script should be imported wherever needed as module.
"""

from models.Contact import Contact
from tabulate import tabulate


def display_contacts(contacts) -> None:
    """
    A module function to display contacts as text output
    ...
    Parameters
    ----------
    contacts : [Contact]
        a list of contact objects to display
    """
    # Convert contact objects to lists and display them in table format using tabulate
    print(tabulate([contact.to_list() for contact in contacts], headers=Contact.supported_search_fields))
