# Vegan Store Management Software

A command-line inventory and sales management application developed in Python
as part of my professional Master's training in Data Science at ProfessionAI.

## Overview

The application manages the inventory and sales operations of a vegan products store,
with persistent storage across different sessions.

The project focuses on core Python programming concepts, including modular programming,
input validation, file handling, and basic application logic.

## Features

- Add new products to the inventory
- Update quantities of existing products
- Display the current inventory
- Register single or multiple product sales
- Validate prices and quantities
- Check stock availability before completing a sale
- Automatically remove out-of-stock products
- Calculate gross and net profits
- Persist inventory and profit data using JSON
- Provide an interactive command-line help menu

## Technical implementation

The application is organized into modular functions responsible for:

- loading and saving data
- validating user input
- managing inventory
- registering sales
- calculating profits
- displaying available commands

Input validation prevents empty product names and invalid or non-positive
numeric values.

Inventory and profit information is stored in a JSON file, allowing data to
persist between program sessions.

## Skills practiced

**Python · Functions · Modular Programming · Input Validation · JSON ·
File Handling · Data Persistence · CLI Applications · Docstrings**

## Context

This project was developed as a hands-on programming assignment within the
[ProfessionAI Data Science Master's program](https://profession.ai/corsi/master-data-science).
