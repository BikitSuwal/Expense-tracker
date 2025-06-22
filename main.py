#Expense tracker project

def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    with open("expenses.txt", "a") as f:
        f.write(f"{name},{category},{amount}\n")
