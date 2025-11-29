arr1 = [
    [2,3],
    [1,5]
]

arr2 = [
    [5,0,3,7,5],
    [9,0,9,1,2]
]

arr3 = [
    [2,1],
    [3,5],
    [7,4],
    [2,6]
]

def into_1d(arr):
    help = []
    x = 0
    while x < len(arr):
        y = 0
        while y < len(arr[x]):
            help.append(arr[x][y])
            y += 1
        x += 1
    return help

def graphics1d(arr):
    for i in arr:
        print(i, end = " ")

graphics1d(into_1d(arr1))
print()
graphics1d(into_1d(arr2))
print()
graphics1d(into_1d(arr3))
print()