"""
ContactRegister Text Module

This script defines display methods for the Text format:
    * display - displays a list of contacts in output text

This script should be imported wherever needed as module.
"""

from models.Contact import Contact
from tabulate import tabulate


def display(contacts) -> None:
    """
    A module function to display contacts as text output
    ...
    Parameters
    ----------
    contacts : [Contact]
        a list of contact objects to display
    """
    # TODO Comment this function
    print(tabulate([contact.to_list() for contact in contacts], headers=Contact.supported_search_fields))
