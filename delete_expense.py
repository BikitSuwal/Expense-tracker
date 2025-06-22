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
