previous_price = float(input("Enter previous price: "))
current_price = float(input("Enter current price: "))
discount = (previous_price - current_price) / previous_price * 100


if discount >= 10:
    print("Buy the product!")
else:
    print("Don't buy the product.")

if discount > 0:
    print(f"Product price reduced by {round(discount,2)}%")
elif discount < 0:
    print(f"Product price increased by {round(discount*-1,2)}%")
else:
    print("Price is the same as it was.")