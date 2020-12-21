"""
ContactRegister JSON Module

This script defines serialisation methods for the JSON format:
    * export_contacts - exports a list of contacts as a .json file
    * import_contacts - imports contacts from a .json file as a list

This script should be imported wherever needed as module.
"""
from models.Contact import Contact
import json


# Define module constants
DATA_FILE = "data/contacts.json"


def export_contacts(contacts) -> str:
    """
    A module function to export contacts to a JSON file
    ...
    Parameters
    ----------
    contacts : [Contact]
        a list of contact objects to export
    ...
    Returns
    -------
    str
        the name of the export file
    """
    # Open the specified file for writing
    with open(DATA_FILE, 'w', newline='') as file:
        # Convert the contacts to dictionaries and dump them to the file as JSON
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)
    return DATA_FILE


def import_contacts() -> [Contact]:
    """
    A module function to import contacts from a JSON file
    ...
    Returns
    -------
    [Contact]
        a list of imported contacts
    """
    # Open the specified file for writing
    with open(DATA_FILE, 'r', newline='') as file:
        # Load the JSON file to dictionaries, creating contact objects from them
        contacts = [Contact.from_dict(data) for data in json.load(file)]
    return contacts
