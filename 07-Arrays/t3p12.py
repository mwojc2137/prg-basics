arr = [2,3,2,5,8,1,9,8]

sin = []
rep = []
unique = []
for row in arr:
    if row not in sin:
        sin.append(row)
    else:
        rep.append(row)

for row in arr:
    if row not in rep:
        unique.append(row)

print(unique)