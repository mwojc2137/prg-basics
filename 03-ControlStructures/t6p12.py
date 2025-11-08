amount = int(input('Numbers of products purchased: '))
price = int(input('Product price: '))

if amount <= 2:
    price = amount*price
else:
    price = 2*price + ((amount-2)*price)*.75

print(f"Amount to pay: {price}")