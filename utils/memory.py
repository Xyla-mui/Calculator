
import os

def update_history(operations: str):
    """Replaces operation words with symbols and saves them to a history file."""
    symbols = {
        "add": "+",
        "sub": "-",
        "multiply": "*",
        "divide": "÷",
        "modulo": "%"
    }

    # Replace operation words with their symbols
    for word, symbol in symbols.items():
        operations = operations.replace(word, symbol)

    # Append the processed operation to the history file
    with open("./utils/history", "a") as file:
        file.write(operations + "\n")


def display_history():
    """Displays all saved calculator operations from the history file."""
    try:
        with open("./utils/history") as file:
            lines = file.readlines()

        if not lines:
            print("History is empty.")
        else:
            for i, line in enumerate(lines, start=1):
                print(f"{i} | {line.strip()}")

    except FileNotFoundError:
        print("No history found.")


def delete_history():
    """Deletes the history file and creates a new empty one."""
    try:
        os.remove("./utils/history")  # Remove the old history file
    except FileNotFoundError:
        pass  # If it doesn’t exist, just ignore the error

    # Create a new empty file for future history
    with open("./utils/history", "x") as f:
        pass

    print("History cleared.")









# this is where th memory management code shoukd be
history = []

# function to add entry to history


def add_to_history(calculation):
    history.append(calculation)
# function to display all history


def show_history():
    if not history:
        print("No history yet.")
    else:
        print("Calculation History:")
        for item in history:
            print(ite