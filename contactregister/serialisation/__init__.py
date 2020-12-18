from helpers import get_module_files


def get_formats() -> [str]:
    return get_module_files(__file__)
