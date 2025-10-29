number = int(input("Number: "))
binary = bin(number)
hexadecimal = hex(number)
print(f"{number} in decimal system is: {binary[2:]} in binary system and {hexadecimal[2:]} in hexadecimal system.")
