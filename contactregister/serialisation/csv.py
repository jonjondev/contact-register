"""
ContactRegister CSV Module

This script defines serialisation methods for the CSV format:
    * export_contacts - exports a list of contacts as a .csv file
    * import_contacts - imports contacts from a .csv file as a list

This script should be imported wherever needed as module.
"""

from models.Contact import Contact
from pathlib import Path
import helpers
import csv
import os


# Define module constants
DATA_FILE = Path(__file__).parent / "../../data/contacts.csv"


def export_contacts(contacts) -> str:
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
    # Try create the file directory and open the specified file for writing
    helpers.try_create_dir(os.path.dirname(DATA_FILE))
    with open(DATA_FILE, 'w', newline='') as file:
        # Set it up for CSV writing
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write the header row, and then rows for each contact
        writer.writerow(Contact.supported_search_fields)
        [writer.writerow(contact.to_list()) for contact in contacts]
    return DATA_FILE


def import_contacts() -> [Contact]:
    """
    A module function to import contacts from a CSV file
    ...
    Returns
    -------
    [Contact]
        a list of imported contacts
    """
    # Open the specified file for reading
    with open(DATA_FILE, 'r', newline='') as file:
        # Set it up for CSV reading
        reader = csv.reader(file, delimiter=',', quotechar='"')
        # Skip the header row, and read in each entry as a contact
        next(reader)
        contacts = [Contact.from_list(row) for row in reader]
    return contacts
