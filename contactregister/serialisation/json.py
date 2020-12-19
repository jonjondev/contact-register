"""
ContactRegister JSON Module

This script defines serialisation methods for the JSON format:
    * export - exports a list of contacts as a .json file

This script should be imported wherever needed as module.
"""

import json


# Define module constants
DATA_FILE = "data/contacts.json"


def export(contacts) -> str:
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
    # TODO Comment this function
    with open(DATA_FILE, 'w', newline='') as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)
    return DATA_FILE
