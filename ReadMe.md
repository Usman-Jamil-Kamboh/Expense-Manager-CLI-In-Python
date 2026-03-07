Expense Manager CLI (Python)






A Command Line Expense Manager built with Python that helps users track income and expenses directly from the terminal.

This project demonstrates modular Python development, JSON data persistence, input validation, and CLI application design.



Features

User creation and management

Add income and expense transactions

View all transaction records

Monthly financial report generation

JSON-based persistent storage

Input validation system

Modular project structure

Project Architecture

Your project follows a modular design, separating responsibilities across different modules.

Expense-Manager-CLI-In-Python
│
├── Main.py
├── MainMenu.py
├── JSON_Defs.py
├── validators.py
│
└── finance
    ├── users.py
    ├── transactions.py
Module Responsibilities
File	Responsibility
Main.py	Program entry point
MainMenu.py	CLI menu logic
users.py	User creation and management
transactions.py	Transaction handling
validators.py	Input validation
JSON_Defs.py	JSON storage structure
