# Calculates sum of digits

def sum(number):
    absnumber = abs(number)
    numsum = 0
    for char in str(absnumber):
        numsum += int(char)
    return numsum

number = int(input("Enter number: "))

print(f'Sum of digits in {number} is {sum(number)}')    
