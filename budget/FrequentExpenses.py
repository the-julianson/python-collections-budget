# First local modules
from . import Expense

# Second, built-in modules
import collections

# Third party modules
import matplotlib.pyplot as plt

# With this I construct the class
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
spending_categories = []


for expense in expenses.list:
    spending_categories.append(expense.category)

# This counter the values, and groups them in a dictionary having the keys with the most ocurrencies as values
spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)

# Separate keys and values into 2 lists
categories, count = zip(*top5)

print(f"All ocurrencies {spending_counter}")
print(f"Most common: {spending_counter.most_common(5)}")
print(categories)
print(count)

# Using matplotlib

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
