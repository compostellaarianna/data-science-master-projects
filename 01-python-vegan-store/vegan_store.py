import json
import os

DATA_FILE = "market_data.json"


def load_data():
    """
    Load inventory and profits from the JSON file.

    Returns:
        tuple: inventory and profits.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        inventory = data.get("inventory", {})
        profits = data.get("profits", {"gross": 0.0, "net": 0.0})
        return inventory, profits
    else:
        inventory = {}
        profits = {"gross": 0.0, "net": 0.0}
        return inventory, profits


def save_data(inventory, profits):
    """
    Save inventory and profits to the JSON file.

    Args:
        inventory (dict): The inventory data.
        profits (dict): The profits data.
    """
    data = {
        "inventory": inventory,
        "profits": profits
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def show_help():
    """
    Print the list of available commands.
    """
    print("The available commands are:")
    print("add: add a product to the inventory")
    print("list: list the products in the inventory")
    print("sale: register a sale")
    print("profits: show total profits")
    print("help: show the available commands")
    print("exit: close the program")


# Below are three validation functions for text, integers, and floating-point values.

def get_valid_text(prompt):
    """
    Read a non-empty text input, stripping spaces and converting to lowercase.
    """
    while True:
        value = input(prompt).strip().lower()  # Removes leading/trailing whitespace and converts the product name to lowercase to prevent duplicate inventory entries caused by inconsistent capitalization.
        if value:
            return value
        print("Invalid input. Please try again.")


def get_valid_int(prompt):
    """
    Read a valid positive integer input.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:  # Ensures that it is also positive.
                return value
            print("Enter a valid positive integer.")
        except ValueError:
            print("Enter a valid integer.")


def get_valid_float(prompt):
    """
    Read a valid positive floating-point input.
    """
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:  # Ensures that it is also positive.
                return value
            print("Enter a valid positive number.")
        except ValueError:
            print("Enter a valid decimal number.")


def add_product(inventory):
    """
    Add a new product to the inventory or update its quantity if it already exists.
    """
    name = get_valid_text("Product name: ")
    quantity = get_valid_int("Quantity: ")
    if name in inventory:
        inventory[name]["quantity"] += quantity
    else:
        buy_price = get_valid_float("Purchase price: ")
        sell_price = get_valid_float("Selling price: ")
        inventory[name] = {
            "quantity": quantity,
            "buy_price": buy_price,
            "sell_price": sell_price
        }

    print(f"ADDED: {quantity} X {name}")


def list_products(inventory):
    """
    List all products in the inventory showing name, quantity, and sale price.
    """
    if not inventory:
        print("No products in the inventory.")
        return

    print("PRODUCT        QUANTITY    PRICE")
    for name, data in inventory.items():
        print(f"{name:<15}{data['quantity']:<11}€{data['sell_price']:.2f}")


def register_sale(inventory, profits):
    """
    Register one or more sold products and update the stock and profits.
    """
    sold_products = []
    sale_total = 0.0
    continue_sale = "yes"

    while continue_sale == "yes":
        while True:
            name = get_valid_text("Product name: ")
            if name in inventory:
                break
            print("Product not found in the inventory.")

        while True:
            quantity = get_valid_int("Quantity: ")
            if quantity <= inventory[name]["quantity"]:
                break
            print("Quantity not available in the inventory.")

        subtotal = quantity * inventory[name]["sell_price"]
        cost = quantity * inventory[name]["buy_price"]

        sold_product = {
            "name": name,
            "quantity": quantity,
            "price": inventory[name]["sell_price"],
            "subtotal": subtotal,
            "cost": cost
        }

        sold_products.append(sold_product)
        sale_total += subtotal
        inventory[name]["quantity"] -= quantity
        if inventory[name]["quantity"] == 0:  # Removes out-of-stock products from the list.
            del inventory[name]

        continue_sale = input("Add another product? (yes/no): ").lower().strip()

        while continue_sale not in ("yes", "no"):  # Handles cases where the response is neither "yes" nor "no".
            print("Invalid response. Enter yes or no.")
            continue_sale = input("Add another product? (yes/no): ").lower().strip()

    total_cost = sum(product["cost"] for product in sold_products)
    profits["gross"] += sale_total
    profits["net"] += sale_total - total_cost

    print("SALE RECORDED")

    for product in sold_products:
        prefix = "- " if len(sold_products) > 1 else ""
        print(f"{prefix}{product['quantity']} X {product['name']}: €{product['price']:.2f}")

    print(f"Total: €{sale_total:.2f}")


def show_profits(profits):
    """
    Show the gross and net profits.
    """
    print(f"Profit: gross=€{profits['gross']:.2f} net=€{profits['net']:.2f}")

inventory, profits = load_data()

while True:
    command = input("Enter a command: ").lower().strip()

    if command == "add":
        add_product(inventory)
        save_data(inventory, profits)  # Save the addition immediately, without waiting until a sale is registered or the program is closed.
    elif command == "list":
        list_products(inventory)
    elif command == "sale":
        register_sale(inventory, profits)
        save_data(inventory, profits)
    elif command == "profits":
        show_profits(profits)
    elif command == "help":
        show_help()
    elif command == "exit":
        save_data(inventory, profits)
        print("Bye bye")
        break
    else:
        print("Invalid command")
        show_help()
