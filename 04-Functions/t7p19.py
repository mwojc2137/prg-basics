def f(n):
    n = str(n)
    list = []
    list2 = []
    sum = 0
    for char in n:
        char = int(char)
        if not char in list:
            list.append(char)
        elif not char in list2:
            sum += 2*char
            list2.append(char)
        else:
            sum += char
    return sum

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))