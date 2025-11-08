decimal = int(input("Enter decimal number: "))

binary = " "

remainder = 0

while decimal > 0:
    remainder = decimal % 2
    decimal = int(decimal/2)
    binary += str(remainder)

reverse = " "

length = len(binary)-1

while length > 0:
    reverse += binary[length]
    length -= 1

print(reverse)