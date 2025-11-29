arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
    [13,14,15]
]

print(arr)

i = 0

while i < len(arr):
    help = arr[i][0]
    arr[i][0] = arr[i][len(arr[i])-1]
    arr[i][len(arr[i])-1] = help
    i += 1

print(arr)