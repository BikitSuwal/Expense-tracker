#Expense tracker project

def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    with open("expenses.txt", "a") as f:
        f.write(f"{name},{category},{amount}\n")

def view_expense():
    with open("expenses.txt", "r") as f:
        lines = f.readlines()
        if not lines:
            print("No expenses recorded yet.")
            return
        print(f"{'Name':<20} {'Category':<15} {'Amount':<10}")
        print("-" * 45)
        for line in lines:
            name, category, amount = line.strip().split(",")
            print(f"{name:<20} {category:<15} {amount:<10}")

def delete_expense():
    with open("expenses.txt", "r") as f:
        lines = f.readlines()
    if not lines:
        print("No expenses to delete.")
        return
    for idx, line in enumerate(lines, 1):
        print(f"{idx}. {line.strip()}")
    num = int(input("Enter the number of the expense to delete: "))
    del lines[num - 1]
    with open("expenses.txt", "w") as f:
        f.writelines(lines)
    print("Expense deleted.")
