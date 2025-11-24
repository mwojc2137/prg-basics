categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

for i in range (len(categories)):
    if expenses[i] == max(expenses):
        print(f"Category {categories[i]} was the most expensive, costing {expenses[i]}")