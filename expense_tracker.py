expenses = []

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
    expenses.append((name, amount))
    print("Expense added.")

  elif choice == "2":
    if not expenses:
      print("No expenses recorded.")
    else:
      for item in expenses:
        print(f"{item[0]} - ${item[1]:.2f}")

  elif choice == "3":
    total = sum(item[1] for item in expenses)
    print(f"Total Spending: ${total:.2f}")

  elif choice == "4":
    print("Goodbye!")
    break

  else:
    print("Invalid choice.")
