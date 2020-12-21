"""
ContactRegister Helper Script

This script contains various helper functions for the contactregister
CLI program and should be imported wherever needed as module.
"""

import os


def get_module_files(file) -> [str]:
    """
    A helper function to return the names of all non-system
    .py files (not __init__, __main__, etc.) in a given module
    ...
    Parameters
    ----------
    file : str
        the __file__ attribute of the specified module
    ...
    Returns
    -------
    [str]
        the list of module file names
    """
    # Get the directory of the file
    dir_path = os.path.dirname(os.path.realpath(file))
    # Get all files in the directory and filter out Python standard module files
    module_files = list(filter(lambda x: not x.startswith("__"), os.listdir(dir_path)))
    # Return filenames stripped of extension
    return [filename.strip('.py') for filename in module_files]


def display_command_options(options, title="Options:") -> None:
    """
    A helper function to enumerate a list of options to the user
    ...
    Parameters
    ----------
    options : str
        a list of options to visually enumerate for the user
    title : str
        a title for the command option display (default is "Options:")
    """
    # Display the title, followed by a list of enumerated options
    print(title)
    [print(f'{i}: {options[i]}') for i in range(0, len(options))]


def get_option_selection(options, prompt="Option: ") -> str:
    """
    A helper function to get integer input from the user based
    on a provided list of enumerated options
    ...
    Parameters
    ----------
    options : str
        a list of options that the user may select
    prompt : str
        a prompt to display (default is "Option: ")
    ...
    Returns
    -------
    str
        the option name as a string
    """
    # Loop until receiving valid input
    selected_option = None
    while selected_option is None:
        try:
            # Get user input as an integer
            selected_option = int(input(prompt).strip())
            # Handle out of bounds case
            if not (-1 < selected_option < len(options)):
                selected_option = None
                print("Input value is out of range, try again")
        # Handle non-integer case
        except ValueError:
            print("Input value not a valid integer, try again")
    # Return the selected option by name
    return options[selected_option]


def parse_query_filters(query) -> [{str: str}]:
    filters = []
    for query_filter in [query_field.split("=", 1) for query_field in query.split(",")]:
        filters.append({"field": query_filter[0].strip(), "pattern": query_filter[1].strip()})
    return filters


class UnknownQueryField(Exception):
    """Raised when searched query field is unknown"""

    def __init__(self, field_name):
        """
        Initialises the class with relevant parameters
        ...
        Parameters
        ----------
        field_name : str
            the name of offending field
        Returns
        -------
        UnknownQueryField
            a new UnknownQueryField object
        """
        self.field = field_name


class MalformedQuery(Exception):
    """Raised when parsed query is malformed"""

    def __init__(self, query):
        """
        Initialises the class with relevant parameters
        ...
        Parameters
        ----------
        query : str
            the value of the malformed query
        Returns
        -------
        MalformedQuery
            a new MalformedQuery object
        """
        self.query = query


class NonexistentFile(Exception):
    """Raised when attempting to import a nonexistent file"""

    def __init__(self, filepath):
        """
        Initialises the class with relevant parameters
        ...
        Parameters
        ----------
        filepath : str
            the missing filepath
        Returns
        -------
        NonexistentFile
            a new NonexistentFile object
        """
        self.filepath = filepath
