from storage import load_expenses, save_expenses

expenses = load_expenses()

def add_expense(name, amount):
  expenses.append({"name": name, "amount": amount})
  save_expenses(expenses)

def view_expenses():
  return expenses

def get_total():
  return sum(exp["amount"] for exp in expenses)
