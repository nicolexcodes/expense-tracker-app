from tracker import add_expense, view_expense, get_total

def menu():
  print("\nExpense Tracker")
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. View Total")
  print("4. Exit")

while True:
  menu()
  choice = input("Choose an option: ")

  if choice == "1":
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    add_expense(name, amount)
    print("Expense added.")

  elif choice == "2":
    expenses = view_expenses()
    if not expenses:
      print("No expenses recorded.")
    else:
      for exp in expenses:
        print(f"{exp['name']} - ${exp['amount']:.2f}")

  elif choice == "3":
    print(f"Total Spending: ${get_total():.2f}")

  elif choice == "4":
    print("Goodbye!")
    break

  else:
    print("Invalid choice.")
