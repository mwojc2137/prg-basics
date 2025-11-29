def identity(n):
    x = []
    for i in range(n):
        y = []
        for j in range(n):
            y.append(0)
        y[i] = 1
        x.append(y)
    return x

def graphics(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    
graphics(identity(3))
print()
graphics(identity(5))
print()
graphics(identity(8))