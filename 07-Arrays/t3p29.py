def create(x,y):
    arr = []
    for i in range (y):
        ar = []
        for i in range(x):
            ar.append(0)
        arr.append(ar)
    return arr

print(create(3,5))