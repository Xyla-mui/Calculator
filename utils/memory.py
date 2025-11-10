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
            print(item)
