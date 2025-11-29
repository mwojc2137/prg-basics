arr = [2,6,4,9,7]

def star(n):
    stars = ""
    for i in range(n):
        stars += "*"
    return stars

for row in arr:
    print(f"{row}: {star(row)}")