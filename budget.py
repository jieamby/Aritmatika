class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return sum(item["amount"] for item in self.ledger)

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.category}")
      category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    title = f"{self.category:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][:23]:23}" + f"{item['amount']:7.2f}" + '\n'
      total += item['amount']
    output = title + items + "Total: " + str(total)
    return output


def create_spend_chart(categories):
  spendings = []
  chart = "Percentage spent by category\n"
  withdrawals = [
      sum(item["amount"] for item in category.ledger if item["amount"] < 0)
      for category in categories
  ]
  total_withdrawals = sum(withdrawals)
  for withdrawal in withdrawals:
    spendings.append(int((withdrawal / total_withdrawals) * 100 // 10) * 10)
  for percentage in range(100, -10, -10):
    chart += str(percentage).rjust(3) + "| "
    for spending in spendings:
      if spending >= percentage:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"
  chart += "    " + "-" * (len(categories) * 3 + 1) + "\n     "
  longest_name_length = max(len(category.category) for category in categories)
  for i in range(longest_name_length):
    for category in categories:
      if len(category.category) > i:
        chart += category.category[i] + "  "
      else:
        chart += "   "
    if i < longest_name_length - 1:
      chart += "\n     "
  return chart
