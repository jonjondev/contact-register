"""
ContactRegister CSV Module

This script defines serialisation methods for the CSV format:
    * export - exports a list of contacts as a .csv file

This script should be imported wherever needed as module.
"""

import models.Contact
import csv


# Define module constants
DATA_FILE = "data/contacts.csv"


def export(contacts) -> str:
    """
    A module function to export contacts to a CSV file
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
        # Set it up for CSV writing
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write the header row, and then rows for each contact
        wr.writerow(models.Contact.Contact.supported_search_fields)
        [wr.writerow(contact.to_list()) for contact in contacts]
    return DATA_FILE
