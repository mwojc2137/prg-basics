def transpose(arr):
    tr = []
    i = 0
    while i < len(arr[0]):
        r = []
        x = 0
        while x < len(arr):
            r.append(arr[x][i])
            x += 1
        tr.append(r)
        i += 1
    return tr

def graphics(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

arr2 = [
    [1,2,3,4,5],
    [6,7,8,9,0]
]

arr3 = [
    [5,6,7,8]
]

graphics(transpose(arr))
print()
graphics(transpose(arr2))
print()
graphics(transpose(arr3))
print()