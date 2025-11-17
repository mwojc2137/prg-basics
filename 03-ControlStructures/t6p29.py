number_of_primes = int(input("Enter, how many primes you want: "))
n = 2
d = 0

primes_found = 0

list = ""

while primes_found < number_of_primes:
    is_prime = True
    for i in range (2,n):
        d = n%i
        if d == 0:
            is_prime = False
    if is_prime == True:
        list += " " + str(n)
        primes_found +=1
    n += 1

print(list)