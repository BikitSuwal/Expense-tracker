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
