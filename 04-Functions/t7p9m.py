def f(n,e):
    sum = 0
    n = str(n)
    if e == True:
        for char in n:
            char = int(char)
            if char%2 == 0:
                sum += char
    if e == False:
        for char in n:
            char = int(char)
            if not char%2 == 0:
                sum += char
    return sum

if __name__ == "__main__":
    print(f(3124, True))