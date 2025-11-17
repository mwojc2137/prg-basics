for i in range (1,8):
    list = ""
    n = 0
    while n < 49:
        list += " " + str(i+n)
        n += 7
    print(list)