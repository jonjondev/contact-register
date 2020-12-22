# ContactRegister

![unittest](https://github.com/J-Mo63/contact-register/workflows/unittest/badge.svg)

ContactRegister is a CLI application for managing contact lists across multiple formats, including text, HTML, CSV, and JSON.

The application provides an API for performing all of these operations, as well as a CLI-based "interactive mode" that can be operated directly from the terminal. The project is well-documented, the structure supports long-term maintainability, and it features fully-modular format extensibility.

The following functionality is currently supported by the ContactRegister API:
- `add_contact(name, address, phone)`
- `get_all_contacts()`
- `search_contacts(query)`
- `display_contacts(display_format)`
- `export_contacts(export_format)`
- `import_contacts(import_format)`

The project currently supports **serialisation to CSV & JSON**, and **displaying to text and HTML**.

## Requirements & Setup

The project requires Python 3.6 or greater and the [`tabulate`](https://pypi.org/project/tabulate/) (v0.8.x) package installed on your machine. This is specified in [`requirements.txt`](requirements.txt) and can be installed using the [pip](https://pypi.org/project/pip/) package manager using the following command:

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

To add a new **display format** simply create a new script in [`contactregister/display`](contactregister/display) with the name `your_format_name.py`. The script should then contain a function with the following method signature, implementing the desired display functionality:
```python
def display_contacts(contacts) -> None:
    ...
```

Likewise, to add a new **serialisation format** simply create a new script in [`contactregister/serialisation`](contactregister/serialisation) with the name `your_format_name.py`. The script should then contain two functions with the following method signatures, implementing the desired serialisation functionality:
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

The project uses Python's inbuilt [unittest](https://docs.python.org/3/library/unittest.html) framework for unit testing. It can be started by running the unittest module from the project's app directory ([`/contactregister`](contactregister)) like so:

```console
$ cd contactregister
$ python -m unittest contactregister_test
......................
--------------------------------------------------------------
Ran 26 tests in 0.411s

OK
```

## Development Experience

In this section I will describe the pitfalls and learnings gained during the development of the project.

In general, I found that while I had some background in the Python language, it became clear during development that some more advanced concepts in Python application structure were necessary areas of improvement for me. This being said, I was still rather judicious with which concepts were applied given their value to the overall design.

### Problems Encountered

- **Application/API Structure:** Early on in development, I spent a good while debating what the final structure of the system should look like. It was stated in the requirements that both a CLI application and API would be needed, however, should they be in separate modules? After creating a series of files, named and commented with functionality - then shuffling them around a bit, I eventually decided to write the main module as the API. The assumption was that it should include a method to run the interactive CLI mode, and if invoked as a program, will run in interactive mode by default.
  

- **Display & Serialisation Modularity:** One of the other requirements specified was extensibility for other developers and easy-to-manage custom formats. The question was in how to approach this problem: using classes and inheritance, or using modules and ducktyping. One thing I felt that would assist in the modularity of the application is to make it so that adding new formats (serialisation or display) would be as simple as adding a new file - no source changes. After some research into Python's abilities in introsepction for classes, I found that it was not sufficient for my purposes, and rather dynamic import of modules would work much better. Using globbing and Python's OS module I was able to make the feature work using filenames. The big learning for me here was to stop avoiding the filesystem modules if they make your life easier and don't negatively affect the final functionality.
  

- **Python's Unit Testing:** This was honestly the most painful part of development for me, as for some reason Python's unittest module was having huge issues with finding any modules using relative Python-paths. I can't say I exactly solved the issue, but after an exhorbitant amount of time diagnosing the issue, I cut my losses and found a temporary solution (`cd`ing into the [`/contactregister`](contactregister) directory before running it).
  

- **Cross-Platform Support:** It turns out that exporting and importing files from a non-module directory in your application can cause issues across platforms, setups and so on. I needed to switch to using generated absoloute paths. The issue was testing. My laptop just runs macOS. My solution was to go ahead and set up CI/CD with a Linux machine using GitHub Actions. Sure enough, doing so revealed a handful of issues, such as directories not automatically being generated during file creation outside of macOS. All the ensuing issues were promptly fixed and the product was made all the more stable for it. From this, I would tell my future self to set up CI/CD testing early.


## Licence

Distributed under the terms of MIT license, see [`LICENCE`](LICENCE) for details.
