import json
import os

FILE_NAME = "expenses.json"


# -----------------------------
# Load saved expenses
# -----------------------------
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


# -----------------------------
# Save expenses
# -----------------------------
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# -----------------------------
# Add an expense
# -----------------------------
def add_expense(expenses):
    print("\n----- ADD EXPENSE -----")

    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Category: ").strip()
    description = input("Description: ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# -----------------------------
# View all expenses
# -----------------------------
def view_expenses(expenses):
    print("\n----- ALL EXPENSES -----")

    if not expenses:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


# -----------------------------
# Calculate total spending
# -----------------------------
def total_spent(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal spent: ₹{total:.2f}")


# -----------------------------
# Category summary
# -----------------------------
def category_summary(expenses):
    print("\n----- CATEGORY SUMMARY -----")

    if not expenses:
        print("No expenses recorded.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# -----------------------------
# Set monthly budget
# -----------------------------
def set_budget():
    try:
        budget = float(input("\nEnter your monthly budget (₹): "))
        print(f"Monthly budget set to ₹{budget:.2f}")
        return budget
    except ValueError:
        print("Invalid budget.")
        return 0


# -----------------------------
# Check remaining budget
# -----------------------------
def budget_remaining(expenses, budget):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    remaining = budget - total

    print("\n----- BUDGET STATUS -----")
    print(f"Budget: ₹{budget:.2f}")
    print(f"Spent: ₹{total:.2f}")
    print(f"Remaining: ₹{remaining:.2f}")

    if remaining < 0:
        print("WARNING: You have exceeded your budget!")
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        print("You are within your budget.")


# -----------------------------
# Main program
# -----------------------------
def main():
    expenses = load_expenses()
    budget = 0

    while True:
        print("\n==============================")
        print("     STUDENT BUDGET TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Category Summary")
        print("5. Set Monthly Budget")
        print("6. Budget Remaining")
        print("7. Exit")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_spent(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            budget = set_budget()

        elif choice == "6":
            budget_remaining(expenses, budget)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-7.")


# Start the program
if __name__ == "__main__":
    main()