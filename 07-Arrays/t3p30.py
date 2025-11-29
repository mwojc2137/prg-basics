arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
] 

x = 0

while x < len(arr):
    y = 0
    while y < len(arr[x]):
        arr[x][y] = (x+1)*(y+1)
        y += 1
    x += 1

print(arr)
        