for i in range (1,10):
    n = 0
    m = ""
    while n <= i:
        if not n == i:
            m += str(i) 
            n += 1
        elif n == i:
            print(m)
            n += 1
