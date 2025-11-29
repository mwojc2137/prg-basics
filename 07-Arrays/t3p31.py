arr = [
    [-38,19],
    [5,40],
    [-7,13],
    [29,16]
]

max = 0
maxx = 0
maxy = 0
min = arr[0][0]
minx = 0
miny = 0

x = 0

while x < len(arr):
    y = 0
    while y < len(arr[x]):
        if arr[x][y] > max:
            max = arr[x][y]
            maxx = x
            maxy = y
        elif arr[x][y] < min:
            min = arr[x][y]
            minx = x
            miny = y
        y += 1
    x += 1

print(f"Largest value is {max}, and is located in column {maxy+1} and row {maxx+1}")
print(f"Smallest value is {min}, and is located in column {miny+1} and row {minx+1}")