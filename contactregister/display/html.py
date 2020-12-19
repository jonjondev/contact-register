"""
ContactRegister HTML Module

This script defines display methods for the HTML format:
    * display - displays a list of contacts in HTML

This script should be imported wherever needed as module.
"""

# Define module constants
DATA_FILE = "data/contacts.html"


def display(contacts) -> None:
    print(f'<display {len(contacts)} contacts in HTML!!!>')
