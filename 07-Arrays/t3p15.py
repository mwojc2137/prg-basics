tuple = (10,20,30,40,50)

rev = []
n = len(tuple)-1
while n >= 0:
    rev.append(tuple[n])
    n -= 1

print(tuple)
print(rev)