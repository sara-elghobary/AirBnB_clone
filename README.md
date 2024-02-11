# HolbertonBnB

The AirBnB clone.

HolbertonBnB is a complete web application, integrating database storage, a back-end API, and front-end interface in a clone of AirBnB.

This team project is part of the ALX Software Engineering program.  
It represents the first step towards building a full web application.

This first step consists of:

- A custom command-line interface for data management,
- The base classes for the storage of this data.

## Files and Directories

- `models` directory contains all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- `tests` directory contains all unit tests.
- `console.py`  is the entry point of our command interpreter.
- `models/base_model.py`  is the base class of all our models. It contains common elements:
    - attributes: `id`, `created_at` and `updated_at`
    - methods: `save()` and `to_json()`
- `models/engine` directory contains all storage classes (using the same prototype). For the moment it has only one: `file_storage.py`.

## Phase One (The console)

The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this we :

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User, State, City, Place…`) that inherit from `BaseModel` .
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all classes and storage engine.
- Manage (create, update, destroy, etc....) objects via a console/command interpreter
- Store and persist objects to files (JSON files).

## Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt **(hbnb)** and waits for the user for input.

|Command|Example|
|---|---|
|Run the console|`./console.py`|
|Quit the console|`(hbnb) quit`|
|Display the help for a command|`(hbnb) help <command>`|
|Create an object (prints its id)|`(hbnb) create <class>`|
|Show an object|`(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)`|
|Destroy an object|`(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)`|
|Show all objects, or all instances of a class|`(hbnb) all` or `(hbnb) all <class>`|
|Update an attribute of an object|`(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")`|

## Tests

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```
