def f(n):
    asterisks = "*"
    for i in range (0,n-1):
        asterisks  += "/*"
    return asterisks

if __name__ == "__main__":
    print(f(4))
    print(f(1))