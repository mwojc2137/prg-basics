def f(n):
    string = ""
    for i in range (1,n+1):
        string += str(i)
    return string

if __name__ == "__main__":
    print(f(11))
    print(f(4))