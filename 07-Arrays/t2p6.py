matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


place = 0
for row in matrix:
    row[place] = 1
    place += 1

for row in matrix:
    for char in row:
        print(char, end = " ")
    print()
