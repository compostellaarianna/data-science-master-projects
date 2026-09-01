# Vegan Store Management Software

A command-line inventory and sales management application developed in Python as part of my
**[professional Master's program in Data Science at ProfessionAI](https://profession.ai/corsi/master-data-science)**.

## Overview

The application manages the inventory and sales operations of a vegan products store,
with persistent storage across different sessions.

The project focuses on core Python programming concepts, including modular programming,
input validation, file handling, and basic application logic.

## Features

- Add new products to the inventory
- Update quantities of existing products
- Display the current inventory
- Register one or multiple product sales
- Validate product names, prices, and quantities
- Check stock availability before completing a sale
- Automatically remove out-of-stock products
- Calculate gross and net profits
- Persist inventory and profit data using JSON
- Display an interactive help menu

## Technical implementation

The application is organized into functions responsible for data persistence,
input validation, inventory management, sales, and profit calculation.

Input validation prevents empty product names and non-positive or invalid numeric values.
Inventory and profit data are stored in `market_data.json`, allowing them to persist
between program sessions.

## Skills practiced

**Python · Functions · Input Validation · JSON · File Handling ·
Data Persistence · CLI Applications · Docstrings**

## Files

- `vegan_store.py` — standalone Python version
- `vegan_store.ipynb` — notebook version
- `market_data.json` — created automatically when the program runs

## Running the application

```bash
python vegan_store.py
```

Available commands:

`add` · `list` · `sale` · `profits` · `help` · `exit`

## Context

This project was developed as a hands-on programming assignment within the
[ProfessionAI Data Science Master's program](https://profession.ai/corsi/master-data-science).
