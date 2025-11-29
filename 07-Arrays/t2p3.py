# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
def category(n):
    totalc = 0
    for row in monthly_expenses:
        totalc += row[n]
    return totalc

def week(n):
    totalw = 0
    for char in monthly_expenses[n]:
        totalw += char
    return totalw

def total():
    total = 0
    for row in monthly_expenses:
        for char in row:
            total += char
    return total

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',category(0))
print('Transport:',category(1))
print('Utilities:',category(2))
print('Week 1:',week(0))
print('Week 2:',week(1))
print('Week 3:',week(2))
print('Week 4:',week(3))
print('---------------')
print('TOTAL:',total())