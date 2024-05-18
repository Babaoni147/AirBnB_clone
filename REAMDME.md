# Airbnb Console Clone

## Table of Contents
- [Description]
- [Features]
- [Installation]
- [Usage]
- [Project Structure]
- [Testing]
- [Contributing]
- [Authors]
- [License]

## Description
The Airbnb Console Clone is a command-line interface (CLI) application that mimics the functionality of the backend of the popular Airbnb platform. This project is designed to help you understand the concepts of Python packages, command interpreters, unit testing, serialization/deserialization, JSON handling, datetime management, and more.
The goal of the project is to deploy on a server a simple copy of the AirBnB website.
It won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

## Features
- Create, read, update, and delete (CRUD) operations for various objects such as users, places, and reviews.
- Command interpreter using the `cmd` module.
- Serialization and deserialization of objects to and from JSON.
- Unit testing to ensure code reliability and correctness.
- Unique identification using UUID.
- Management of `datetime` objects.

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/AirBnB_clone.git
   cd AirBnB_clone
# Execution
The shell will work like this in interactive mode:

        $ ./console.py
        (hbnb) help

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit

        (hbnb)
        (hbnb)
        (hbnb) quit
        $

But also in non-interactive mode: (like the Shell project in C)

        $ echo "help" | ./console.py
        (hbnb)

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit
        (hbnb)
        $
        $ cat test_help
        help
        $
        $ cat test_help | ./console.py
        (hbnb)

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit
        (hbnb)
        $

## Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* update - Updates an instance based on the class name and id
* quit/EOF - quit the console
* help - see descriptions of commands

## Usage

-AirBnB_clone$ ./console.py
    (hbnb)

## Create
To create an object use format "create <ClassName>" ex:

        (hbnb) create BaseModel

## Show
To show an instance based on the class name and id. Ex:

        (hbnb) show BaseModel 1234-1234-1234.

## Destroy
To Delete an instance of an object use "destroy <ClassName> id". Ex:

        (hbnb) destroy BaseModel 1234-1234-1234.

## All
all or all <class name> Ex:

        (hbnb) all or all State

## Update
Updates an instance based on the class name and id:

        (hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"

## Quit
quit or EOF

## Help
help or help <command> Ex:

        (hbnb) help or help quit
         Defines quit option
        (hbnb)

# Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

## < Project Structure>

AirBnB_clone/
│
├── console.py         # Main entry point for the command interpreter
├── models/            # Package containing the model classes
│   ├── base_model.py  # BaseModel class definition
│   ├── user.py        # User class definition
│   └── __init__.py    # Package initialization
│
├── tests/             # Unit tests for the project
│   ├── test_base_model.py  # Unit tests for the BaseModel class
│   ├── test_user.py        # Unit tests for the User class
│   └── __init__.py         # Package initialization
│
├── requirements.txt   # Dependencies for the project
├── AUTHORS            # List of project contributors
└── README.md          # This README file

# Authors
Ohwoka Emmanuel <emmyprime2015@gmai.com>
