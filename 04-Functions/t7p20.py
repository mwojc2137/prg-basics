def f(n):
    primes = []
    x = 2
    while len(primes) < n:
        is_prime = True 
        for i in range (2,x):
            d = x%i
            if d == 0:
                is_prime = False
        if is_prime == True:
            primes.append(x)
        x += 1
    return primes[len(primes)-1]
        
if __name__ == "__main__":
    print(f(69))