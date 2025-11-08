amount = int(input("Enter amount in PLN: "))

coins5 = int(amount/5)
coins2 = int((amount%5)/2)
coins1 = int(((amount%5)%2))

print(f"{amount}PLN in coins:")
print(f"5PLN coins: {coins5}")
print(f"2PLN coins: {coins2}")
print(f"1PLN coins: {coins1}")