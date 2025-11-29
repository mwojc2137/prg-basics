arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

notrepeat = []

for char in arr1:
    if char not in arr2:
        notrepeat.append(char)

unique = ""
for char in notrepeat:
    unique += str(char) + " "

print(unique)