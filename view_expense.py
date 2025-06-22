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
