import os


def get_module_files(file) -> [str]:
    dir_path = os.path.dirname(os.path.realpath(file))
    module_files = list(filter(lambda x: not x.startswith("__"), os.listdir(dir_path)))
    return [filename.strip('.py') for filename in module_files]


def display_command_options(options, title="Options:") -> None:
    print(title)
    [print(f'{i}: {options[i]}') for i in range(0, len(options))]
