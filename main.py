#Expense tracker project

def add_expense():
    name = input("Enter expense name: ").strip()
    while not name:
        print("Expense name cannot be empty.")
        name = input("Enter expense name: ").strip()

    category = input("Enter category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    while True:
        amount = input("Enter amount: ").strip()
        try:
            amount_float = float(amount)
            if amount_float < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for amount.")

    with open("expenses.txt", "a") as f:
        f.write(f"{name},{category},{amount_float}\n")

def view_expense():
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No expenses recorded yet.")
                return
            print(f"{'Name':<20} {'Category':<15} {'Amount':<10}")
            print("-" * 45)
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, category, amount = parts
                    print(f"{name:<20} {category:<15} {amount:<10}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def delete_expense():
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No expenses to delete.")
            return
        for idx, line in enumerate(lines, 1):
            print(f"{idx}. {line.strip()}")
        while True:
            num = input("Enter the number of the expense to delete: ").strip()
            if not num.isdigit():
                print("Please enter a valid number.")
                continue
            num = int(num)
            if 1 <= num <= len(lines):
                break
            else:
                print(f"Please enter a number between 1 and {len(lines)}.")
        del lines[num - 1]
        with open("expenses.txt", "w") as f:
            f.writelines(lines)
        print("Expense deleted.")
    except FileNotFoundError:
        print("No expenses to delete.")

def total_expenses():
    total = 0.0
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    try:
                        amount = float(parts[2])
                        total += amount
                    except ValueError:
                        continue
        print(f"Total expenses: Rs {total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")
