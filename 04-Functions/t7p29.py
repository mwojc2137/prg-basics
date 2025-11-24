def factorial(n):
    result = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range (1,n+1):
            result *= i
    return result

if __name__ == "__main__":
    print(factorial(5))