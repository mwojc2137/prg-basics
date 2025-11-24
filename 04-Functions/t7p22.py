def f(n):
    n = str(n).strip()
    acronym = n[0]
    p = 0
    for char in n:
        if char == " ":
            acronym += n[p+1]
        p += 1
    return acronym

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
    print(f(" jakis text 1221"))
