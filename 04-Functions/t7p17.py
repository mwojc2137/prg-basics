def f(n):
    n = str(n)
    reverse = ""
    r = 1
    for char in n:
        reverse += n[len(n)-r]
        r += 1
    if n == reverse:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("radar")) 
    print(f("12-11-21")) 
    print(f("book")) 
    print(f("123454321"))
