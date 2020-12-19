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
    # TODO Comment this function
    dir_path = os.path.dirname(os.path.realpath(file))
    module_files = list(filter(lambda x: not x.startswith("__"), os.listdir(dir_path)))
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
    # TODO Comment this function
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
    """
    # TODO Comment this function
    selected_option = None
    while not selected_option:
        try:
            selected_option = int(input(prompt).strip())
        except ValueError:
            print("Input value not an integer, try again")
        if selected_option >= len(options):
            selected_option = None
            print("Input value is out of range, try again")
    return options[selected_option]
