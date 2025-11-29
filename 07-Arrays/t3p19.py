arr = [1,2,33,534,32,2,6,342,1,234,34,23]
value = int(input("Enter number: "))

count = 0
for row in arr:
    if row > value:
        count += 1

print (count)