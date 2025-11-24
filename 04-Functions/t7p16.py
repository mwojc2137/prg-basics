def f(n):
    fibonacci = [0, 1]
    for i in range (1,n-1):
        fibonacci.append(fibonacci[len(fibonacci)-2] + fibonacci[len(fibonacci)-1])
    return fibonacci[len(fibonacci)-1]

if __name__ == "__main__":
    print(f(5)) 
    print(f(9)) 
    print(f(200)) 
    print(f(13))