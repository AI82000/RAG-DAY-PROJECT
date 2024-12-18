expenditures = {}

def show_expenditures():
    """Display all expenditures."""
    if not expenditures:
        print("No expenditures recorded yet.")
    else:
        print("\n--- Rag Day Expenditures ---")
        for item, amount in expenditures.items():
            print(f"{item}: ${amount}")
        print("----------------------------")

def add_expenditure():
    """Add a new expenditure."""
    item = input("Enter the name of the expenditure item: ")
    try:
        amount = float(input(f"Enter the amount spent on {item}: $"))
        expenditures[item] = amount
        print(f"{item} has been added with an amount of ${amount}.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def edit_expenditure():
    """Edit an existing expenditure."""
    item = input("Enter the name of the expenditure item to edit: ")
    if item in expenditures:
        try:
            new_amount = float(input(f"Enter the new amount for {item}: $"))
            expenditures[item] = new_amount
            print(f"The amount for {item} has been updated to ${new_amount}.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    else:
        print(f"No expenditure found for {item}.")

def delete_expenditure():
    """Delete an existing expenditure."""
    item = input("Enter the name of the expenditure item to delete: ")
    if item in expenditures:
        del expenditures[item]
        print(f"{item} has been deleted.")
    else:
        print(f"No expenditure found for {item}.")

def exit_program():
    """Exit the program."""
    print("Exiting the program. Goodbye!")
    return False

def main():
    """Main function to run the expenditure program."""
    while True:
        print("\n--- Rag Day Expenditure Tracker ---")
        print("1. Show Expenditures")
        print("2. Add Expenditure")
        print("3. Edit Expenditure")
        print("4. Delete Expenditure")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_expenditures()
        elif choice == '2':
            add_expenditure()
        elif choice == '3':
            edit_expenditure()
        elif choice == '4':
            delete_expenditure()
        elif choice == '5':
            if not exit_program():
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()