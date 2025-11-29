arr1 = [4,5,6,7,4,3,2,5]
arr2 = [0,1,2,3,4,5,6,7,8,9]

subset = True
for row in arr1:
    if row not in arr2:
        subset = False

print(subset)