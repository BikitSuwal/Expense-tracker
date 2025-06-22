from add_expense import add_expense
from view_expense import view_expense
from delete_expense import delete_expense
from total_expense import total_expenses
from expense_logger import setup_logger  

def menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total Expenses")
    print("5. Exit")

def main():
    setup_logger() 
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
