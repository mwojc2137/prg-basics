tuple = (50,20,40,50,30,50)

value = 50

count = 0

for row in tuple:
    if row == value:
        count += 1

print("Number of occurences: ", count)