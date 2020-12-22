# ContactRegister

![unittest](https://github.com/J-Mo63/contact-register/workflows/unittest/badge.svg)

ContactRegister is a CLI application for managing contact lists across multiple formats, including text, HTML, CSV, and JSON.

The application provides an API for performing all of these operations, as well as a CLI-based "interactive mode" that can be operated directly from the terminal.
The project is well-documented, the structure supports long-term maintainability, and it features fully-modular format extensibility.

The following functionality is currently supported by the ContactRegister API:
- `add_contact(name, address, phone)`
- `get_all_contacts()`
- `search_contacts(query)`
- `display_contacts(display_format)`
- `export_contacts(export_format)`
- `import_contacts(import_format)`

The project currently supports **serialisation to CSV & JSON**, and **displaying to text and HTML**.

## Requirements & Setup

The project requires Python 3.6 or greater and the [`tabulate`](https://pypi.org/project/tabulate/) (v0.8.x) package installed on your machine.
This is specified in [`requirements.txt`](requirements.txt) and can be installed using the [pip](https://pypi.org/project/pip/) package manager using the following command:

```console
$ pip install -r requirements.txt
```

## Usage

Once setup, the project can most easily be run as an interactive session by running the `contactregister` module from the project root like so:

```console
$ python contactregister
```

### Adding New Display & Serialisation Formats

The project has been built to support dynamic addition of display and serialisation formats.

To add a new **display format** simply create a new script in [`contactregister/display`](contactregister/display) with the name `your_format_name.py`.
The script should then contain a function with the following method signature, implementing the desired display functionality:
```python
def display_contacts(contacts) -> None:
    ...
```

Likewise, to add a new **serialisation format** simply create a new script in [`contactregister/serialisation`](contactregister/serialisation) with the name `your_format_name.py`. 
The script should then contain two functions with the following method signatures, implementing the desired serialisation functionality:
```python
def export_contacts(contacts) -> str:
    ...

def import_contacts() -> [Contact]:
    ...
```

For further details on implementing custom formats, please read through the format scripts provided.

### Project Structure

```
[root]
    |-[contactregister] <- application module
    |     |
    |     |-[display] <- display format scripts by format name (e.g. html.py)
    |     |
    |     |-[serialisation] <- serialisation scripts by format name (e.g. json.py)
    |     |
    |     |-[models] <- model classes used by the application
    |     |
    |     |- contactregister.py <- main application script, contains API methods
    |     |
    |     |- contactregister_test.py <- application unit tests
    |     |
    |     |- helpers.py <- application helper functions and classes
    |
    |- requirements.txt <- Python package dependency list
```

## Testing

The project uses Python's inbuilt [unittest](https://docs.python.org/3/library/unittest.html) framework for unit testing.
It can be started by running the unittest module from the project's app directory ([`/contactregister`](contactregister)) like so:

```console
$ cd contactregister
$ python -m unittest contactregister_test
......................
--------------------------------------------------------------
Ran 26 tests in 0.411s

OK
```

## Licence

Distributed under the terms of MIT license, see [`LICENCE`](LICENCE) for details.
