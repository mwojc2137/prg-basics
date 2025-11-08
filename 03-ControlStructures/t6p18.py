x = int(input("x = "))
y = int(input("y = "))

if x == 0 or y == 0:
    if not x == 0:
        print(f"Point ({x},{y}) is on the x axis")
    elif not y == 0:
        print(f"Point ({x},{y}) is on the y axis")
    else: 
        print(f"Point ({x},{y}) is the start of coordinate system")
elif x > 0:
    if y > 0:
        print(f"Point ({x},{y}) is in the first quadrant")
    else:
        print(f"Point ({x},{y}) is in the second quadrant")
else:
    if y < 0:
        print(f"Point ({x},{y}) is in the third quadrant")
    else:
        print(f"Point ({x},{y}) is in the fourth quadrant")