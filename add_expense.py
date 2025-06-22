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
