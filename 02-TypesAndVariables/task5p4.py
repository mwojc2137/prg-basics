#calculates vat from total price instead of just value 

total_price = input('Enter the price')
total_price = float(total_price)
vat = total_price/123*23
amount = total_price/123*100
amount = round(amount, 2)
vat = round(vat,2)
print(f'Amount: {amount}')
print(f'Vat: {vat}')