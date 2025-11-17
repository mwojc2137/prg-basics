n = 1
d = 0

while True:
    is_prime = True
    for i in range (2,n):
        d = n%i
        if d == 0:
            is_prime = False
    if is_prime == True:
        print(n)
    n += 1

